::

        _/      _/    _/_/    
       _/_/  _/_/  _/    _/   
      _/  _/  _/  _/_/_/_/    
     _/      _/  _/    _/     
    _/      _/  _/    _/      
                            


Step 1 - Preparation
====================

- Go to bitbucket: https://bitbucket.org/mawork/ma-django-skeleton/downloads
- Click on *Branches*
- Click on *zip* for the branch you want to download. As explanation:
    - *master* contains a django project, including the hot shit like
      bower, requirejs, sass etc..
    - *basic-django* contains a raw django project with simple css and
      javascript files setup.
- Unpack the downloaded zip into a new, empty project directory



Step 2 - Set Project up on SVN
==============================

- Login to the Granger server and run the following set of commands::

    ssh granger@68.178.206.139 
    Gr_102666KUMA
    su - 
    svnadmin create /svnroot/(projectName)
    chmod 777 -R /svnroot/(projectName)
    exit

    (you are finished on the Granger server for now)



Step 3 - import the cloned local prject to SVN
==============================================

- Locally 'cd' into the project directory if your not already there::

    svn import svn+ssh://granger@68.178.206.139/svnroot/(projectName) -m "initial import"

- enter the password for the Granger server::

    Gr_102666KUMA



Step 4 - Clean up and Checkout the new project
==============================================

- Locally remove the initial setup project and trash it::

    cd ../
    rm -r (projectName)

- Using Versions create a new Bookmark and Checkout using the following general settings::

    (Angelo:)
    svn+ssh://68.178.206.139/svnroot/(projectName)
    username: granger
    password: Gr_102666KUMA

    (Martin:)
    svn+ssh://68.178.206.139/svnroot/(projectName)
    username: martin
    password: ma040978work

 

Step 5 - Initial setup and running the project
==============================================

- 'cd' into the project directory and run::

    fab devinit

- this will download all python and javascript dependencies, compile sass, etc..
- local project should be running as usual/expected

.. note::

    If something in the projects changes, like dependencies or the sass files,
    you can retrigger the build with ``fab devupdate``.



Step 6 - Initialising the new project on the server
===================================================

- open project.ini file in your text editior.
- fill out the project 'name' setting::

    name = (projectName)

- fill out the ``host`` setting as well. This is where the project shall be
  installed later. You can choose from:

  - ``maworaa1.miniserver.com``
  - ``maworaa3.miniserver.com``

- set ``domain`` accordingly:

  - for **maworaa1** choose: ``%(name)s.maworaa.co.uk``
  - for **maworaa3** choose: ``%(name)s.madebyma.com``

- then run::

    (Angelo:)
    fab -u angelo install
    102666GHOST (enter the MySQL password on Maworaa1 & Maworaa3)
    ghostranch (enter your user account password on Maworaa1/Maworaa2) (old pwd: nabadu38)

    (Martin:)
    fab -u martin install
    102666GHOST (enter the MySQL password on Maworaa1 & Maworaa3)
    kexede29 / MA280976work (enter your user account password on Maworaa1/Maworaa3)

- Shell output should return the following::

    Success!
    http://projec1.maworaa.co.uk/

    The project should be up and running. You will find the local_settings.py used on the server on your local machine as server_settings.py in the current working directory. Modify it as needed and upload again with:
    fab conf:put

.. note:: *(only do this if you've modified the server_settings.py file) - also do NOT commit this file to SVN.*



Step 7 - LAUNCH - Changing the domain
=====================================

- When your ready to switch to the live domain open up your 'project.ini' file and edit the following line::

    domain = %(name)s.maworaa.co.uk

- Save and commit this file to svn then run::

    fab -u angelo setup

- You should also then commit the file to the main SVN repo::

    deploy


- NOTE: Media & Static settings will be broken now because the domain has changed, you need to log into Maworaa and change the 'local_setting.py' file to the correct domain::

    MEDIA_URL = 'http://media.project2.maworaa.co.uk/'
    STATIC_URL = 'http://static.project2.maworaa.co.uk/'


NOTES - adding more domains to the config domain
================================================

If you want to add another domain to the config:
	
- open: config/nginx.conf.template
- Add the new domain to line #18 and #44 - something like this::

    server_name www.%(DOMAIN)s lightshow.com;

- (make sure to keep the 's' after %(DOMAIN))
- Then push changes to the server::

    fab -u angelo setup	



FEATURE: loaddata + loadmedia
=============================

- When you want to take data from the server for your local project run the following:
  (change the 'project.ini' 'loaddata_apps =' to add new Apps to the loaddata config)

  ::

    (Angelo:)
    fab -u angelo loaddata
    nabadu38

    (Martin:)
    fab -u martin loadata
    ma040978work

- When you want to take media from the server for your local project run the following::

    (Angelo:)
    fab -u angelo loadmedia
    nabadu38

    (Martin:)
    fab -u martin loadmedia
    ma040978work



CURRENT QUIRKS
==============

1: If

(if using auto-reload) when you 'quit the server' you might need to run this::
	
    pkill -f runserver
    or
    pkill (if you have the alias setup)

then you can run it again as usual...

You can switch Autoreload off in the django toolbar.


==============================================

::
                                                  
        _/        _/  _/  _/                      
       _/  _/        _/  _/    _/_/    _/  _/_/   
      _/_/      _/  _/  _/  _/_/_/_/  _/_/        
     _/  _/    _/  _/  _/  _/        _/           
    _/    _/  _/  _/  _/    _/_/_/  _/            
                                        
