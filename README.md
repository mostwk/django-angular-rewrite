[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)
[![Build Status](https://travis-ci.com/mostwk/django-angular-rewrite.svg?branch=master)](https://travis-ci.com/mostwk/django-angular-rewrite)
[![Coverage Status](https://coveralls.io/repos/github/mostwk/django-angular-rewrite/badge.svg?branch=master)](https://coveralls.io/github/mostwk/django-angular-rewrite?branch=master)

Settings
========

Moved to
[settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

Basic Commands
==============

Type checks
-----------

Running type checks with mypy:

    $ mypy django_rewrite

Test coverage
-------------

### Running tests with py.test and generating coverage report
    $ cd django_rewrite
    $ pytest --cov

Live reloading and Sass CSS compilation
---------------------------------------

Moved to [Live reloading and SASS
compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

Celery
------

This app comes with Celery.

To run a celery worker:

``` {.sourceCode .bash}
cd django_rewrite
celery -A config.celery_app worker -l info
```

Deployment
==========

The following details how to deploy this application.

Docker
------

See detailed [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
