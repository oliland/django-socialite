import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1
SITE_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)))
USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = ''

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'nha8r+&$d&i0dsz#mk2tg2@0nbde+ozzwrjnthe=+t1uzq5e(5'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'socialite.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'oauth_access',
    'facebookuser',
    'linkedinuser',
    'twitteruser',
    'utils',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'facebookuser.backends.FacebookBackend',
    'twitteruser.backends.TwitterBackend',
    'linkedinuser.backends.LinkedInBackend',
    )

from local import *
