#AskPupkin

Example web project for my Technopark study.

## Installation

### DB

You can use ``fill_db`` Django command to perform filling DB with random data. Because of large amount of data, we use ``LOAD DATA INFILE`` MySQL statement which needs ``FILE`` privilege.

    GRANT FILE ON *.* TO askpupkin@localhost;

After that you may execute this:

    ./manage.py fill_db

### Search

To install Sphinx search, execute this:

    # ln -s ~/git/ask-pupkin/conf/sphinx-search.conf /etc/sphinxsearch/ask-pupkin.conf

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

###Question page:

![question](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-question.png)

###Button design:

![button](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-button.png)
![button](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-button-hover.png)
![button](https://raw.githubusercontent.com/quasiyoke/ask-pupkin/master/doc/img/screenshot-button-active.png)
