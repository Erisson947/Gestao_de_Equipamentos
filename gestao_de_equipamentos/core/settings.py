"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from os import getenv
from pathlib import Path
from django.contrib.messages import constants

from celery.schedules import crontab
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env', override=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(getenv('DEBUG', 1)))

ALLOWED_HOSTS = [
    host.strip() for host in getenv('ALLOWED_HOSTS', '').split(',')
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',
    'django_htmx',
    'widget_tweaks',
    'django_celery_results',
    'django_celery_beat',

    # Social Auth
    'social_django',

    
    'usuarios',
    'equipamentos',
    'laboratorios',
    'pegar_chave',
    'notificacoes',
    'rolepermissions',
    'notifications',
    'multiselectfield',
    'bootstrap_datepicker_plus',
    'tempus_dominus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
    'django_htmx.middleware.HtmxMiddleware',

    # Social Auth
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base' / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Social Auth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': getenv('DB_ENGINE', ''),
        'NAME': getenv('DB_NAME', ''),
        'USER': getenv('DB_USER', ''),
        'PASSWORD': getenv('DB_PASSWORD', ''),
        'HOST': getenv('DB_HOST', ''),
        'PORT': getenv('DB_PORT', ''),
    }
}

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
    },
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

AUTHENTICATION_BACKENDS = (
    'suap.backends.SuapOAuth2',  # Backend do SUAP
    'django.contrib.auth.backends.ModelBackend',
)


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_TZ = True


MESSAGE_TAGS = {
    constants.DEBUG: 'message-debug',
    constants.ERROR: 'message-error',
    constants.INFO: 'message-info',
    constants.SUCCESS: 'message-success',
    constants.WARNING: 'message-warning',
}

TEMPUS_DOMINUS_DATE_FORMAT = 'DD/MM/YYYY'

AUTH_USER_MODEL = 'usuarios.User'
USER_FIELDS = [
    'registration',
    'campus',
    'course',
    'full_name',
    'personal_email',
    'school_email',
    'academic_email',
    'cpf',
    'link_type',
    'sex',
    'date_of_birth',
    'photo1',
    'photo2',
    'is_admin',
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'base' / 'static',
]
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROLE_PERMISSIONS_MODULE = 'core.roles'


# Chaves da aplicação SUAP
SOCIAL_AUTH_SUAP_KEY=getenv('SOCIAL_AUTH_SUAP_KEY', '')
SOCIAL_AUTH_SUAP_SECRET=getenv('SOCIAL_AUTH_SUAP_SECRET', '')

CELERY_BROKER_URL = 'amqp://Erisson:ecmm2609@127.0.0.1:5672'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True


CELERY_TIMEZONE = 'America/Recife'
CELERY_IMPORTS = ['pegar_chave.tasks']
CELERY_BEAT_SCHEDULE = {
'checar_chaves_atrasadas': {

    'task': 'pegar_chave.tasks.checar_chaves_atrasadas',
    'schedule': crontab(minute=0, hour=0), #every day at midnight
},
}

CELERY_RESULT_BACKEND = 'django-db'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = False
EMAIL_PORT = 587
EMAIL_HOST_USER = 'erissoncarlos926@gmail.com'
EMAIL_HOST_PASSWORD = 'yqohfdxzjfnkqdsz'