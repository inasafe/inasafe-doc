# ~/fabfile.py
# A Fabric file for carrying out various administrative tasks with InaSAFE.
# Tim Sutton, Jan 2013

import os
from fabric.api import *
from datetime import datetime
from fabric.contrib.files import contains, exists, append, sed
import fabtools
from fabtools import require
from fabgis import fabgis
# Don't remove even though its unused
from fabtools.vagrant import vagrant

# Usage for localhost commands:
# fab localhost [command]
#  e.g. fab localhost update
# To run remotely do
#  fab remote [command]
# e.g.
# fab -H 188.40.123.80:8697 show_environment
# To run on a vagrant vhost do
# fab vagrant show_environment
#  e.g. fab vagrant show_environment
#
# Note: Vagrant tasks will only run if they @task decorator is used on
#       the function. See show_environment function below.

# Usage fab localhost [command]
#    or fab remote [command]
#  e.g. fab localhost initialise_qgis_plugin_repo

# Global options
env.env_set = False


def _all():
    """Things to do regardless of whether command is local or remote."""
    if env.env_set:
        fastprint('Environment already set!\n')
        return

    fastprint('Setting environment!\n')
    # Key is hostname as it resolves by running hostname directly on the server
    # value is desired web site url to publish the repo as.
    doc_site_names = {
        'cunonia': 'inasafe-docs.localhost',
        'waterfall': 'inasafe-docs.localhost',
        'spur': 'inasafe-docs.localhost',
        'maps.linfiniti.com': 'inasafe.linfiniti.com',
        'linfiniti': 'inasafe-docs.linfiniti.com',
        #vagrant instance
        'vagrant-inasafe-doc': 'inasafe-docs.vagrant.localhost',
        'shiva': 'docs.inasafe.org'}

    with hide('output'):
        env.user = run('whoami')
        env.hostname = run('hostname')
        if env.hostname not in doc_site_names:
            print 'Error: %s not in: \n%s' % (env.hostname, doc_site_names)
            exit()
        else:
            env.doc_site_name = doc_site_names[env.hostname]
            env.inasafe_release_web_path = (
                '\/var\/www\/inasafe-release-documentation')
            env.inasafe_master_web_path = (
                '\/var\/www\/inasafe-master-documentation')
            env.home = os.path.join('/home/', env.user)
            env.repo_path = os.path.join(env.home, 'dev', 'python')
            env.git_url = 'git://github.com/AIFDR/inasafe-doc.git'
            env.repo_alias = 'inasafe-doc'
            env.code_path = os.path.join(env.repo_path, env.repo_alias)

    env.env_set = True
    fastprint('env.env_set = %s' % env.env_set)

###############################################################################
# Next section contains helper methods
###############################################################################


def get_webdir(branch):
    if 'master' == branch:
        webdir = env.inasafe_master_web_path
    else:
        webdir = env.inasafe_release_web_path
    return webdir


@task
def build_doc(branch='master'):
    """Create a pdf and html doc tree and publish them online.
    Args:
        branch: str - a string representing the name of the branch to build
            from. Defaults to 'master'.
    To run e.g.::
        fab -H 188.40.123.80:8697 build_documentation
        or to package up a specific branch (in this case minimum_needs)
        fab -H 88.198.36.154:8697 build_documentation:version-1_1
    .. note:: Using the branch option will not work for branches older than 1.1
    """
    _all()
    fabgis.setup_inasafe()
    # Needed for when running on headless servers
    fabtools.require.deb.package('xvfb')
    fabgis.install_qgis1_8()

    sudo('pip install Sphinx')

    fabgis.update_git_checkout(
        code_path=env.repo_path,
        url=env.git_url,
        repo_alias=env.repo_alias,
        branch=branch)
    fabgis.setup_latex()

    dir_name = os.path.join(env.repo_path, env.repo_alias)
    with cd(dir_name):
        # build the Documentation
        run('chmod +x scripts/post_translate.sh')
        run('xvfb-run scripts/post_translate.sh')


@task
def deploy_docs_site(branch='master'):
    """Initialise an InaSAFE docs site where we host docs and pdf."""
    _all()
    build_doc()

    fabtools.require.deb.package('apache2')
    code_path = env.code_path
    webdir = get_webdir(branch)

    inasafe_docs_apache_conf = '%s.inasafe-docs.conf' % branch
    inasafe_docs_apache_conf_template = 'inasafe-docs.conf.templ'

    if not exists(webdir):
        sudo('mkdir -p %s/pdf' % webdir)
        sudo('chown -R %s.%s %s' % (env.user, env.user, webdir))

    apache_path = '/etc/apache2/sites-available/'
    with cd(apache_path):
        if not exists(inasafe_docs_apache_conf):
            local_dir = os.path.dirname(__file__)
            local_file = os.path.abspath(os.path.join(
                local_dir,
                'scripts',
                inasafe_docs_apache_conf_template))
            put(local_file,
                "/etc/apache2/sites-available/%s" %
                inasafe_docs_apache_conf_template,
                use_sudo=True)

        my_tokens = {
            'SERVERNAME': env.doc_site_name,  # Web Url e.g. foo.com
            'WEBMASTER': 'werner@linfiniti.com',  # email of web master
            'DOCUMENTROOT': webdir,  # Content root .e.g. /var/www
        }
        fabgis.replace_tokens(inasafe_docs_apache_conf_template, my_tokens)

    with cd(code_path):
        # Copy built Documentation to the Webserver path
        run('cp -r docs/output/html/* %s' % webdir)
        run('cp -r docs/output/pdf %s' % webdir)
        run('cp scripts/.htaccess %s' % webdir)
        run('cp scripts/directory*.html %s/en/_static/' % webdir)

    # Add a hosts entry for local testing - only really useful for localhost
    hosts = '/etc/hosts'
    if not contains(hosts, 'inasafe-docs'):
        append(hosts, '127.0.0.1 %s' % env.doc_site_name, use_sudo=True)

    sudo('a2ensite inasafe-docs.conf')
    sudo('a2enmod rewrite')
    sudo('service apache2 reload')


@task
def setup_jenkins(use_upstream_repo=True, branch='master'):
    """

    :param use_upstream_repo:
    :param branch:
    :return:
    """
    _all()

    # We need some additional tools to run jenkins checks
    fabtools.require.deb.package('xvfb')
    fabtools.require.deb.package('pep8')
    fabtools.require.deb.package('pylint')
    fabtools.require.deb.package('pyflakes')
    fabtools.require.deb.package('sloccount')

    fabgis.initialise_jenkins_site(use_upstream_repo=use_upstream_repo)
    fabgis.install_jenkins(use_upstream_repo)
    setup_jenkins_jobs(branch=branch)


@task
def setup_jenkins_jobs(branch='master'):
    """

    :param branch:
    :return:
    """
    _all()
    xvfb_config = "org.jenkinsci.plugins.xvfb.XvfbBuildWrapper.xml"
    job_dir = ['InaSAFE-Documentation']
    with cd('/var/lib/jenkins/'):
        if not exists(xvfb_config):
            local_dir = os.path.dirname(__file__)
            local_file = os.path.abspath(os.path.join(
                local_dir,
                'scripts',
                'jenkins_jobs',
                xvfb_config))
            put(local_file,
                "/var/lib/jenkins/", use_sudo=True)

    with cd('/var/lib/jenkins/jobs/'):
        for job in job_dir:
            if not exists(job):
                local_dir = os.path.dirname(__file__)
                local_job_file = os.path.abspath(os.path.join(
                    local_dir,
                    'scripts',
                    'jenkins_jobs',
                    '%s.xml') % job)
                sudo('mkdir /var/lib/jenkins/jobs/%s' % job)
                put(local_job_file,
                    "/var/lib/jenkins/jobs/%s/config.xml" % job,
                    use_sudo=True)
        sudo('chown -R jenkins:nogroup InaSAFE*')
    sudo('service jenkins restart')
    webdir = get_webdir(branch)
    fabtools.require.directory(webdir, use_sudo=True, owner='jenkins')
