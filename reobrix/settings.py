"""
Django settings for reobrix project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

from decouple import config



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p22(+szg+i9_1o(xdjk3%@n9-gtuy*^2aq8qg1b2l=p%!t$b7w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # False

ALLOWED_HOSTS = ['*'] # ALLOWED_HOSTS = [] # if local



CART_SESSION_ID = 'cart'




SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    # 3rd party
    'django.contrib.postgres',
    'taggit',
    'ckeditor',
    'ckeditor_uploader',
    'django_celery_results',
    'django_recaptcha',

    # my apps
    'core',
    'blog', # or 'blog.apps.BlogConfig',
    'shop',
    'cart',
    'orders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reobrix.urls'

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
                'cart.context_processors.cart',
                'core.context_processors.business_info',
                'shop.context_processors.categories',
                'core.context_processors.current_view_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'reobrix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # 'django.db.backends.mysql' in pythonanywhere and 'django.db.backends.postgresql'
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
		'TEST': {'NAME': config('TEST_DB_NAME'),}
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # if local develop this can be omitted.

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Media files: newly added
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = BASE_DIR / 'media'

'''
# old version

# Celery Configuration Options
CELERY_BROKER_URL = 'pyamqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'rpc://'

# Celery Configuration Options
CELERY_TIMEZONE = "Australia/Tasmania"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
'''


# reobrix/settings.py
# CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_BROKER_URL = 'amqps://xydayzfd:T4tBPBAwl11HqSsEriTGj8sia69oIYY1@cougar.rmq.cloudamqp.com/xydayzfd'
CELERY_RESULT_BACKEND = 'django-db'  # or another result backend


# CELERY_RESULT_BACKEND = 'rpc://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'









PRODUCTS_PER_PAGE = 6  # Set the default number of products per page
POSTS_PER_PAGE = 3  # Set the default number of products per page


# Email server configuration
EMAIL_HOST = 'smtp.qq.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')




# Add reCAPTCHA keys
RECAPTCHA_PUBLIC_KEY = '6LdCAQkqAAAAAEOG66b6hMOsEE_F1-huNeaUbCE7'
RECAPTCHA_PRIVATE_KEY = '6LdCAQkqAAAAAPpOLoVTHDJp-AWIo5l2_dOo6fep'





# Settings for CKEditor in your Django settings file
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'full',
        'extraPlugins': ','.join([
            'codesnippet',
            'widget',
            'dialog',
            'mathjax',  # add other plugins as needed
        ]),
        'codeSnippet_theme': 'monokai_sublime',  # Example code snippet theme
    },
}