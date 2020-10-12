=====
Usage
=====

To use Django page hits in a project:

1. Add *'django_page_hits'* at the end of **INSTALLED_APPS**.

2. Add *'django_page_hits.middleware.PageHitsMiddleware'* to end of **MIDDLEWARE_CLASSES**.

3. Run `python manage.py syncdb` or `python manage.py migrate`.

4. A new app is registered to admin panel.
