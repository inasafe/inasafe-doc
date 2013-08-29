# ~/fabfile.py
"""A Fabric file for carrying out various administrative tasks with InaSAFE.

e.g.::

    fab -H foo:1234 setup_docs_web_site

.. note:: Vagrant tasks will only run if they @task decorator is used on
   the function. See show_environment function below.

Tim Sutton, Jan 2013
"""

import os
from fabric.api import task, fastprint, run, sudo, cd, put, env
from fabric.contrib.files import contains, exists, append, upload_template
from fabric.colors import green, blue
import fabtools
from fabtools import require
from fabtools.service import restart
from fabgis.qgis import install_qgis1_8
from fabgis.jenkins import jenkins_deploy_website, install_jenkins
from fabgis.git import update_git_checkout
from fabgis.inasafe import setup_inasafe
# noinspection PyUnresolvedReferences
from fabgis.docker import (
    setup_docker,
    create_docker_container,
    get_docker_port_mappings,
    current_docker_container)
from fabgis.sphinx import setup_latex, setup_sphinx, setup_transifex
from fabgis.system import create_user
# Don't remove even though its unused
# noinspection PyUnresolvedReferences
from fabtools.vagrant import vagrant

# Global options
repo_path = os.path.join(os.path.dirname(__file__), 'dev', 'python')
code_path = os.path.join(repo_path, 'inasafe-doc')
web_directory = os.path.join('/', 'var', 'www', 'inasafe-org')


@task
def build_docs(branch='master'):
    """Create a pdf and html doc tree and publish them online.

    :param branch: The name of the branch to build from. Defaults to 'master'.
    :type branch: str

    To run e.g.::

        fab -H 188.40.123.80:8697 build_docs
        or to package up a specific branch (in this case minimum_needs)
        fab -H 88.198.36.154:8697 build_docs:version-1_1

    .. note:: Using the branch option will not work for branches older than 1.1
    """
    fastprint(blue('Running build docs task.'))
    setup_inasafe()
    # Needed for when running on headless servers
    fabtools.require.deb.package('xvfb')
    fabtools.require.deb.package('rpl')
    install_qgis1_8()

    setup_sphinx()
    setup_transifex()
    setup_latex()

    update_git_checkout(
        code_path=repo_path,
        url='git://github.com/AIFDR/inasafe-doc.git',
        repo_alias='inasafe-doc',
        branch=branch)
    setup_latex()

    with cd(code_path):
        # build the Documentation
        run('chmod +x scripts/post_translate.sh')
        run('xvfb-run scripts/post_translate.sh')


@task
def setup_web_user():
    """Set up a user called web inside the container."""
    create_user('web')


@task
def setup_docs_web_proxy():
    """Set up a mod proxy based vhost to forward web traffic to internal host.

    If container_id is none, it will also install docker and set up the
    entire documentation web site inside that docker container.

    """
    container_id = current_docker_container()
    if container_id is None:
        setup_docker()
        container_id = create_docker_container(image='fabgis/sshd')
        port_mappings = get_docker_port_mappings(container_id)
        ssh_port = port_mappings[22]
        run('fab -H root@%s:%i setup_web_user' % (env.host, ssh_port))
        run('fab -H web@%s:%i setup_docs_web_site' % (env.host, ssh_port))
    else:
        port_mappings = get_docker_port_mappings(container_id)

    http_port = port_mappings[80]

    fabtools.require.deb.package('apache2')
    sudo('a2enmod proxy proxy_http')

    context = {
        'internal_host': env.host,
        'internal_port': http_port,
        'server_name': 'inasafe.org'
    }

    apache_conf_template = 'inasafe-doc.conf.templ'
    apache_path = '/etc/apache2/sites-available/'

    # Clone and replace tokens in apache conf

    local_dir = os.path.dirname(__file__)
    local_file = os.path.abspath(os.path.join(
        local_dir,
        'scripts',
        apache_conf_template))

    fastprint(green('Using %s for template' % local_file))

    destination = '%s/inasafe.org' % apache_path

    upload_template(
        local_file,
        destination,
        context=context,
        use_sudo=True)

    require.apache.enable('a2ensite inasafe.org')
    restart('apache2')


@task
def setup_docs_web_site(branch='master'):
    """Initialise an InaSAFE docs site where we host docs and pdf.

    :param branch: Which branch of the documentation to build.
    :type branch: str

    """
    build_docs()

    fabtools.require.deb.package('apache2')

    apache_conf_template = 'inasafe-doc.conf.templ'

    if not exists(web_directory):
        sudo('mkdir -p %s/pdf' % web_directory)
        # TODO: Fix perms below
        #sudo('chown -R %s.%s %s' % (user, user, web_directory))

    apache_path = '/etc/apache2/sites-available/'

    # Clone and replace tokens in apache conf

    local_dir = os.path.dirname(__file__)
    local_file = os.path.abspath(os.path.join(
        local_dir,
        'scripts',
        apache_conf_template))

    context = {
        'server_name': 'inasafe.org',  # Web Url e.g. foo.com
        'web_master': 'info@inasafe.org',  # email of web master
        'document_root': web_directory,  # Content root .e.g. /var/www
    }

    fastprint(green('Using %s for template' % local_file))

    destination = '%s/inasafe-docs.conf' % apache_path

    upload_template(
        local_file,
        destination,
        context=context,
        use_sudo=True)

    with cd(code_path):
        # Copy built Documentation to the Webserver path
        run('cp -r docs/output/html/* %s' % web_directory)
        run('cp -r docs/output/pdf %s' % web_directory)
        run('cp scripts/.htaccess %s' % web_directory)
        run('cp scripts/directory*.html %s/en/_static/' % web_directory)

    # Add a hosts entry for local testing - only really useful for localhost
    hosts = '/etc/hosts'
    if not contains(hosts, 'inasafe-docs'):
        append(hosts, '127.0.0.1 inasafe-doc.localhost', use_sudo=True)

    require.apache.enable('a2ensite inasafe-docs.conf')
    sudo('a2enmod rewrite')
    restart('apache2')


@task
def setup_jenkins(use_upstream_repo=True, branch='master'):
    """Setup a jenkins build job to build the docs.

    :param use_upstream_repo: Whether to use apt package for jenkins or the
        upstream original installer.
    :type use_upstream_repo: bool

    :param branch: Which branch of the documentation to build.
    :type branch: str
    """
    # We need some additional tools to run jenkins checks for documentation
    fabtools.require.deb.package('xvfb')
    fabtools.require.deb.package('pep8')
    fabtools.require.deb.package('pylint')
    fabtools.require.deb.package('pyflakes')
    fabtools.require.deb.package('sloccount')

    jenkins_deploy_website(use_upstream_repo=use_upstream_repo)
    install_jenkins(use_upstream_repo)
    setup_jenkins_jobs(branch=branch)


@task
def setup_jenkins_jobs(branch='master'):
    """Uploads the prepared jobs into jenkins for testing.

    :param branch: Which branch of the documentation to build.
    :type branch: str
    """
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
                    '%s.xml' % job))
                sudo('mkdir /var/lib/jenkins/jobs/%s' % job)
                put(local_job_file,
                    "/var/lib/jenkins/jobs/%s/config.xml" % job,
                    use_sudo=True)
        sudo('chown -R jenkins:nogroup InaSAFE*')
    sudo('service jenkins restart')
    fabtools.require.directory(web_directory, use_sudo=True, owner='jenkins')
