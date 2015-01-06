#AskPupkin

Example web project for my Technopark study.

## Installation

Installation was described for Debian-based systems.

### Requirements

AskPupkin uses [Django-Sphinx](https://github.com/dcramer/django-sphinx) for search.

To install Apache and mod-wsgi

    # apt-get install apache libapache2-mod-wsgi

### Apache configuration
	
Debian-based systems have especial system for managing Apache confs. Directory ``/etc/apache2/mods-available/`` contains config file's ``/etc/apache2/apache2.conf`` fragments belonging to different mods. a2dismod / a2enmod utilities can be used to create symlinks to needed fragments at ``/etc/apache2/mods-enabled/`` directory to turn on / off needed Apache extensions.

WSGI mod should be turned on by default.

To turn on mod-prefork, you need to turn off mod-event:

    # a2dismod mpm_event
    # a2enmod mpm_prefork

To turn sites' configs on:

    $ cd ~/git/
    $ git clone https://github.com/quasiyoke/ask-pupkin.git

    # ln -s ~/git/ask-pupkin/conf/ask-pupkin-simple-wsgi-site.conf /etc/apache2/sites-available/ask-pupkin-simple-wsgi-site.conf
    # a2dissite 000-default
    # a2ensite ask-pupkin-simple-wsgi-site

To force Apache to listen 8080 port, you need to add the following directive to ``ports.conf``:

    Listen 8080

To use Apache as web server for Django-project, add this config ``conf/ask-pupkin-site.conf`` to possible sites:

    # ln -s ~/git/ask-pupkin/conf/ask-pupkin-site.conf /etc/apache2/sites-available/ask-pupkin-site.conf

You can activate it, desactivating previous configuration before the following way:

    # a2dissite ask-pupkin-simple-wsgi-site
    # a2ensite ask-pupkin-site

To make configuration changes work, execute this:

    # apache2ctl restart

### Nginx

To setup Nginx:

    # apt-get install nginx

After that remove the following directive from Apache's ``ports.conf``:

    Listen 80

Make the symlink to Nginx'es conf file at ``/etc/nginx/sites-available``:

    # ln -s ~/git/ask-pupkin/conf/ask-pupkin-site-nginx /etc/nginx/sites-available/ask-pupkin

Turn on site's conf:

    # rm /etc/nginx/sites-enabled/default
    # ln -s /etc/nginx/sites-available/ask-pupkin /etc/nginx/sites-enabled/ask-pupkin

### Directories

Folders for users' uploads should have right permissions.

    $ chgrp -R www-data uploads
    $ chmod -R g+w uploads

### DB

You can use ``fill_db`` Django command to perform filling DB with random data. Because of large amount of data, we use ``LOAD DATA INFILE`` MySQL statement which needs ``FILE`` privilege.

    GRANT FILE ON *.* TO askpupkin@localhost;

After that you may execute this:

    ./manage.py fill_db

### Search

To install Sphinx search, execute this:

    CREATE USER sphinx@localhost IDENTIFIED BY 'topsecret';
    GRANT ALL ON askpupkin.* TO sphinx@localhost;

    $ mysql -uroot -ptopsecret \askpupkin < sphinx-search-view.sql
    # ln -s ~/git/ask-pupkin/conf/sphinx-search.conf /etc/sphinxsearch/ask-pupkin.conf
    # indexer --all --config /etc/sphinxsearch/ask-pupkin.conf
    # sudo mkdir /var/run/sphinxsearch
    # searchd --config /etc/sphinxsearch/ask-pupkin.conf

## Screenshots

###Home page:

![home page](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot.png)

###Hot questions page:

![hot questions](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-hot-questions.png)

###Sign up page:

![sign up](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-signup.png)

###Incorrect sign up data:

![incorrect sign up data](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-signup-incorrect.png)

###Login page:

![login](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-login.png)

###Incorrect login data:

![incorrect login data](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-login-incorrect.png)

###Logout page:

![logout](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-logout.png)

###Profile editing page:

![profile editing page](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-profile-edit.png)

###Question page:

![question](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-question.png)

###Button design:

![button](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-button.png)
![button](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-button-hover.png)
![button](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-button-active.png)
