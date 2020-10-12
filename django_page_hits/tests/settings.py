SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "django_page_hits",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_page_hits_test.sqlite3',
    }
}
