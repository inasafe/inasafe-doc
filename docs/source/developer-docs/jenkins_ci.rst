===========================================
Continuous Integration Testing with Jenkins
===========================================

.. note:: This documentation is Copyright Linfiniti Consulting CC. May 2013
   and has been included here to provide provenance, and adapted for the
   |project_name| project.

`Jenkins <http://jenkins-ci.org/>`_ is an automated build and test server.

Installation procedure - Jenkins server
---------------------------------------

If you want to have the most recent version of jenkins the install procedure
is described at http://pkg.jenkins-ci.org/debian/.

*You can skip the following part if you want to use jenkins that comes with
your Distribution:*

To start, do this::

   wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -

Now add this to your :file:`/etc/apt/sources.list`::

   deb http://pkg.jenkins-ci.org/debian binary/

In any case you will install jenkins with::

   sudo apt-get update
   sudo apt-get install jenkins

Finishing this jenkins can now be viewed looking at
http://localhost:8080/

If you already have a running instance of Apache on your Server or you want
to run several other pages too you might want to integrate the instance of
jenkins into apache.

If apache is not installed you can install apache::

   sudo apt-get install apache2

To integrate jenkins into apache you need to configure

DNS and Reverse Proxy
.....................

The following example uses hostname as a placeholder for your FQDN.
In most cases (running on your own machine) hostname will be localhost.

Create a virtual host on the server's apache installation to reverse
proxy by creating this file:
:file:`/etc/apache2/sites-available/jenkins.hostname.conf` which should
contain::

   <VirtualHost *:80>
     ServerAdmin yourname@hostname
     ServerName jenkins.hostname

     ProxyPass         / http://localhost:8080/
     ProxyPassReverse  / http://localhost:8080/
     ProxyRequests     Off

     # Local reverse proxy authorization override
     # Most unix distribution deny proxy by default
     # (ie /etc/apache2/mods-enabled/proxy.conf in Ubuntu)
     <Proxy http://localhost:8080/*>
       Order deny,allow
       Allow from all
     </Proxy>
     # Possible values include: debug, info, notice, warn, error, crit,
     # alert, emerg.
     LogLevel warn

     ErrorLog /var/log/apache2/jenkins.hostname.error.log
     CustomLog /var/log/apache2/jenkins.hostname.access.log combined
     ServerSignature Off

   </VirtualHost>

To use this Proxy on localhost we have to enable two apache Modules in the
installation.

To do so do::

   sudo a2enmod proxy
   sudo a2enmod proxy_http

Now enable this vhost::

   sudo a2ensite jenkins.hostname.conf

Depending on your distribution you have to restart apache either using::

 sudo /etc/init.d/apache reload

or::

 service apache2 reload

Configure the server
--------------------

Go to http://jenkins.hostname and log in as an admin user.

Enable Plugins
..............

:menuselection:`Jenkins --> Manage Jenkins --> Manage Plugins` or go to
http://jenkins.hostname/pluginManager/.

Enable the following plugins:

* GitHub plugin
* Xvfb Plugin
* Violations
* Status Monitor Plugin
* Jenkins Sounds plugin
* SLOCCount Plugin
* dashboard-view
* Cobertura Plugin
* Coverage Complexity Scatter Plot PlugIn

That should also resolve some other plugins as dependencies and install them.

If you are using other private repositories on your server you might want to
lock down jenkins to make everything private and only give some people admin
rights.

Lock down access
................

We are hosting private repositories on the server so we want to make everything
private. To do that we do:
:menuselection:`Jenkins --> Manage Jenkins --> Configure System` or go to
http://jenkins.linfiniti.com/configure.

Under :guilabel:`Access control - Security Realm`, check
:guilabel:`Jenkins's own user database`.

Under :guilabel:`Authorization` check
:guilabel:`Project-based Matrix Authorization Strategy`, then add your admin
users only here, giving them all permissions. We will add less privileged
users on a project by project basis.


Other Configuration options
...........................

* :guilabel:`Jenkins URL` set to :kbd:`http://jenkins.linfiniti.com/`
* :guilabel:`Sender E-mail Address` set to
  :kbd:`Linfiniti Jenkins <jenkins@linfiniti.com>`
* :guilabel:`GitHub Web Hook` set to :kbd:`Manually manage hook URLs`


Creating the Jenkins |project_name| Job
---------------------------------------

Create a new Job (project):

:menuselection:`Jenkins --> New Job` or go to
http://jenkins.linfiniti.com/view/All/newJob.

Here is a log of the options we set for the Jenkins job:

* :guilabel:`Project Name` set to :kbd:`InaSAFE` (don't use spaces for the
  project name!).
* Check :guilabel:`Enable project-based security` then add an entry for
  **Anonymous** with :kbd:`Job: Read` and :kbd:`Job Discover` permissions
  only. This will allow anonymous read-only access to the project.
* :guilabel:`Xvfb` set to ticked.
* :guilabel:`GitHub project` set to :kbd:`https://github.com/AIFDR/inasafe/`
* :guilabel:`Source Code Management` check :guilabel:`Git` and set to
  :kbd:`git@github.com:AIFDR-AusAID/inasafe.git`
* :guilabel:`Branch Specifier (blank for default)` set to :kbd:`master`
* :guilabel:`Repository browser` set to :kbd:`auto`
* :guilabel:`Build Triggers` set to
  :kbd:`Build when a change is pushed to GitHub` - this will cause the project
  to build every time a new commit is pushed to GitHub. We also need to setup
  a GitHub hook to do this which is described further down.

**Build Actions**

* :guilabel:`Build` add an :kbd:`Execute Shell` step and set the script as
  follows::

       export PYTHONPATH=/usr/local/qgis-1.8/share/qgis/python/
       export LD_LIBRARY_PATH=/usr/local/qgis-1.8/lib
       export QGIS_PREFIX_PATH=/usr/local/qgis-1.8/

       # Make sure data dir is current and synced it its git clone
       scripts/update-test-data.sh

       #Go on with metrics and tests
       make jenkins-pyflakes
       make jenkins-pep8
       make jenkins-pylint
       make jenkins-sloccount
       make jenkins-test

.. note:: In this server instance we are using a hand built QGIS. The initial
   3 export lines may not be needed if you are using a package build QGIS
   installation.

* :guilabel:`Add build step` set to :kbd:`play a sound` and choose a sound
  which will play when the build completes (optional)

**Post-build Actions**

Add the following actions and settings:

* :guilabel:`Publish Cobertura Coverage Report` set
  :guilabel:`Cobertura xml report pattern` to :kbd:`coverage.xml`.
  For the rest take the defaults or tweak them as you like.
* :guilabel:`Publish JUnit test result report` set :guilabel:`Test report XMLs`
   to :kbd:`nosetests.xml`. I also disabled
   :guilabel:`Retain long standard output/error` (you can enable it temporarily
   while debugging server side build issues).
* :guilabel:`Publish SLOCCount analysis reports` set
  :guilabel:`SLOCcount reports` to :kbd:`sloccount.sc`
* :guilabel:`Report Violations` set the following:
   * :guilabel:`pep8` to :kbd:`pep8.log`
   * :guilabel:`pylint` to :kbd:`pylint.log`
* :guilabel:`Email notification` set :guilabel:`Recipients` to
  :kbd:`tim@linfiniti.com`. Add any additional recipients as
  needed (space delimited). Also I set :guilabel:`Send e-mail for every
  unstable build` checked
  and :guilabel:`Send separate e-mails to individuals who broke the build`
  checked.
* :guilabel:`Jenkins Sounds` set :guilabel:`Failure` to :kbd:`argh(wave)`
* :guilabel:`Jenkins Sounds` set :guilabel:`Success` to :kbd:`Yahoo.Yodel(wave)`
* :guilabel:`Publish Coverage / Complexity Scatter Plot` check
  :guilabel:`Locate the graph at the topmost of Jenkins project page`
* :guilabel:`Status Monitor` enable (this is optional)

Click :guilabel:`Save`

Server Configuration in the shell
---------------------------------

We need to do the following on the server as the jenkins user:

Create an ssh key for Jenkins
.............................

This key will be used to enable Jenkins access to private repos on GitHub. You
only need to do this once on the server for each project::

   sudo su - jenkins
   jenkins@maps:~$ ssh-keygen
   Generating public/private rsa key pair.
   Enter file in which to save the key (/var/lib/jenkins/.ssh/id_rsa_inasafe):
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   Your identification has been saved in /var/lib/jenkins/.ssh/id_rsa_inasafe.
   Your public key has been saved in /var/lib/jenkins/.ssh/id_rsa_inasafe.pub.
   The key fingerprint is:
   29:7e:b6:f5:18:5e:cb:e7:f6:b7:84:e1:f5:66:31:41 jenkins@maps.linfiniti.com
   The key's randomart image is:
   +--[ RSA 2048]----+
   |               E |
   | .            .  |
   |               . |
   |         .      .|
   |      . S    . + |
   |     . .    . + +|
   |      . o o .o .+|
   |       o + * .+o.|
   |        . o ++.o+|
   +++++++++++++++++++


Here's our key::

   cat .ssh/id_rsa_inasafe.pub
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5f7il/lmIUQeIrcQ3f10krOOjLSwPhpJB5G6T
   LG1Dtxoyb/o/XgxPOjNfVfoVNLhB7AVp6I/IsrK3KvO8wkuOVWQ5Q5p3ntPnT6eX62JTLAlPeOGo
   MX0Iq1Vs6cOAhNK11uMfXwdUk//cht3zSlb6GLeg7mTNw/JGPAzJV4YkCcIK87H3e1ClYEU+7Kzb
   lbGKBfXWxgUPIHVRfwVZJZwbCgt1hBSBs7nJFmLqC654rRxhpFAWi72/Go79AW+YEDWUOOSZEsGc
   aT0kJ4mrks0nOMwAhcimcFqfdmmwOqIXgLPm/1jG78z08zGYhNiLOcaZDj1ULnQNmAtDx0/rCOuL
   jenkins@maps.linfiniti.com

You need to create an ssh host alias so that when doing a git checkout, the
correct keypair is used. Add this to the :file:`~/.ssh/config` of the jenkins
user::

   Host |project_name|GitHub
        IdentityFile /home/jenkins/.ssh/id_rsa_inasafe
        HostName github.com

Now go to https://github.com/AIFDR/inasafe/admin/keys and add the above
key as a deploy key.

Next we add the github key to the Jenkins user's allowed hosts. The easiest way
to do this is just to make a temporary clone of the repo. Again this only needs
to be done once and then Jenkins will work for all github projects.

Back on the server::

   jenkins@maps:~$ cd /tmp/
   jenkins@maps:/tmp$ git clone git@InaSAFEGithub:AIFDR-AusAID/inasafe.git
   Cloning into inasafe...
   The authenticity of host 'github.com (207.97.227.239)' can't be established.
   RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
   Are you sure you want to continue connecting (yes/no)? yes

Also you should set the Jenkins git user and email::

   jenkins@maps:~$ git config --global user.email "jenkins@linfiniti.com"
   jenkins@maps:~$ git config --global user.name "Jenkins Build Server"

.. note:: The source tree will be in :file:`~/jobs/InaSAFE/workspace/`.

Project setup
.............

Try to do an initial build. It will fail because we have to copy the
|project_name| test data into the job directory. Use the same procedure as
above to add ad deploy key to the inasafe-data repo and then clone it (as
jenkins user)::

   cd ~/jobs/InaSAFE/
   git clone git@InaSAFEDataGitHub:timlinux/inasafe-data.git

GitHub Hook Setup
.................

In GitHub hooks, enable Jenkins (GitHub plugin) and set the url to::

   http://jenkins.linfiniti.com/github-webhook/

Testing on Jenkins server
.........................

Simply commit something and push it to the server. Turn the speakers on
on your desktop with the Jenkins page (http://jenkins.linfiniti.com) open
and you should hear a cheer or a groan depending on whether the test passes
or fails.

Further Reading
---------------

Here are some useful resources we found while getting things set up.

* http://www.alexconrad.org/2011/10/jenkins-and-python.html
* http://hustoknow.blogspot.com/2011/02/setting-up-django-nose-on-hudson.html
* http://blog.jvc26.org/2011/06/13/jenkins-ci-and-django-howto
* https://sites.google.com/site/kmmbvnr/home/django-jenkins-tutorial (probably
  the most useful article I found)
* http://blog.mathieu-leplatre.info/django-et-jenkins-fr.html (in French)
