================
Django page hits
================


.. image:: https://img.shields.io/pypi/v/django_page_hits.svg
        :target: https://pypi.python.org/pypi/django_page_hits

.. image:: https://img.shields.io/travis/amritghimire/django_page_hits.svg
        :target: https://travis-ci.com/amritghimire/django_page_hits

.. image:: https://readthedocs.org/projects/django-page-hits/badge/?version=latest
        :target: https://django-page-hits.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/amritghimire/django_page_hits/shield.svg
     :target: https://pyup.io/repos/github/amritghimire/django_page_hits/
     :alt: Updates



A middleware which stores the records of page view counts


* Free software: MIT license
* Documentation: https://django-page-hits.readthedocs.io.


Installation
------------


1. Install from github or clone the repository:
    `pip install django_page_hits`

2. Add *'django_page_hits'* at the end of **INSTALLED_APPS**.

3. Add *'django_page_hits.middleware.PageHitsMiddleware'* to end of **MIDDLEWARE_CLASSES**.

4. Run `python manage.py syncdb` or `python manage.py migrate`.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
