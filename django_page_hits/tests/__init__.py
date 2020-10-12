"""Unit test package for django_page_hits."""
import os

import django
from django.core.management import call_command

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_page_hits.tests.settings'
django.setup()
call_command('flush', '--no-input')
call_command('migrate')
