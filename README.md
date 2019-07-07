[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)
[![Build Status](https://travis-ci.com/mostwk/django-angular-rewrite.svg?branch=master)](https://travis-ci.com/mostwk/django-angular-rewrite)


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

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Running tests with py.test

    $ pytest

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
