"""
Django settings for DEMOPROJECT project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from .email_info import *
import os
import django_heroku
from wagtail.embeds.oembed_providers import youtube

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#11yayz=k%wd-5(evc8s%h1j^u*o$8z#^bjv9=d^i!2iv&*k^z'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# DEBUG = False
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'DEMOAPP.apps.DemoappConfig',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sitemaps',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',

    'django.contrib.staticfiles',
    'mathfilters',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'blog',
    'modelcluster',
    'taggit',

    'captcha',
    'wagtailcaptcha',
    'ckeditor',
]
# pip freeze > requirements.txt
# pip install -r requirements.txt
# py -3.7 -m venv myenvpy manage

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'DEMOPROJECT.middleware.LoginRequiredMiddleware',
    'compression_middleware.middleware.CompressionMiddleware',
]

ROOT_URLCONF = 'DEMOPROJECT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'DEMOPROJECT.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fort',
        'USER': 'postgres1',
        'PASSWORD': 'BrightSpark:234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# _______for another machine take these steps_______ #
# delete all migrations
# delete local postgres table

# might have to manage.py makemigrations DEMOAPP

# might have to manage.py migrate DEMOAPP

# might have to comment out models.py in demoapp
# python manage.py migrate --run-syncdb

# might have to recomment back in the models.py
# python manage.py makemigrations
# python mange.py migrate
# python manage.py migrate --run-syncdb

# python manage.py loaddata db.json


# python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e
#       auth.permission -e wagtailcore.groupcollectionpermission --indent 4 > db.json
# python manage.py loaddata db.json


# if on pgadmin follow the tutorial to backup as sql file and then as tar file
# then restore tar file into other machine's pgadmin


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# List of finder classes that know how to find static files in
# various locations.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'DEMOPROJECT/static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'DEMOPROJECT/media')]

WAGTAIL_SITE_NAME = 'Fortress website'

EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT
EMAIL_BACKEND = EMAIL_BACKEND

WAGTAIL_FRONTEND_LOGIN_URL = '/login/'

LOGIN_URL = '/login'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 2
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_BLACKLIST = ["admin"]
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
LOGIN_REDIRECT_URL = '/'

# Recaptcha settings
RECAPTCHA_PUBLIC_KEY = "6LdT_dsUAAAAAH2cTbodfKOVXYOgKbd4ys18wzzf"
RECAPTCHA_PRIVATE_KEY = "6LdT_dsUAAAAANpNL07g_0pkSTz2zDlpq-v_K_uc"
NOCAPTCHA = True

WAGTAILEMBEDS_RESPONSIVE_HTML = True

# Add a custom provider
# Your custom provider must support oEmbed for this to work. You should be
# able to find these details in the provider's documentation.
# - 'endpoint' is the URL of the oEmbed endpoint that Wagtail will call
# - 'urls' specifies which patterns
my_custom_provider = {
    'endpoint': 'https://customvideosite.com/oembed',
    'urls': [
        '^http(?:s)?://(?:www\\.)?customvideosite\\.com/[^#?/]+/videos/.+$',
    ]
}

# videos uploaded to youtube and then shared as an embed URL into a rich text field
WAGTAILEMBEDS_FINDERS = [
    {
        'class': 'wagtail.embeds.finders.oembed',
        'providers': [
            {
                "endpoint": "https://www.youtube.com/oembed",
                "urls": [
                    r'^https?://(?:[-\w]+\.)?youtube\.com/watch.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/v/.+$',
                    r'^https?://youtu\.be/.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/user/.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/[^#?/]+#[^#?/]+/.+$',
                    r'^https?://m\.youtube\.com/index.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/profile.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/view_play_list.+$',
                    r'^https?://(?:[-\w]+\.)?youtube\.com/playlist.+$',
                ],
            }
        ],
        'options': {'scheme': 'https'}
    },
    {
        'class': 'wagtail.embeds.finders.oembed',
    }
]

GOOGLE_RECAPTCHA_SECRET_KEY = "6LdT_dsUAAAAANpNL07g_0pkSTz2zDlpq-v_K_uc"

# Activate Django-Heroku.
django_heroku.settings(locals())

# test
# python3.7 must be used
