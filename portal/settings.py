"""
Django settings for portal project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-c16&bg(921m=(fl685x&e9)l8$alz7swyidm*21&_d(%#@-$4r',
)

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
    if host.strip()
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogue',
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

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portal.wsgi.application'

# ── Database ─────────────────────────────────────────────────────────
# Falls back to SQLite if real credentials are not set in .env.
# When real credentials are present, uses PostgreSQL with the pycsw
# schema so Django tables are created where we have write permission.

_gis_db_user = os.environ.get('GIS_DB_USER', '')

if _gis_db_user and _gis_db_user not in ('', 'YOUR_DB_USER'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.environ.get('GIS_DB_HOST', 'gisdb.systra.info'),
            'PORT': os.environ.get('GIS_DB_PORT', '5432'),
            'NAME': os.environ.get('GIS_DB_NAME', 'uk_irl'),
            'USER': _gis_db_user,
            'PASSWORD': os.environ.get('GIS_DB_PASSWORD', ''),
            'OPTIONS': {
                'sslmode': os.environ.get('GIS_DB_SSLMODE', 'require'),
                'options': '-c search_path=p_pycsw,public',
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Systra GIS Portal — catalogue / storage configuration ───────────

PYCSW_STAC_URL = os.environ.get('PYCSW_STAC_URL', 'mock')

GIS_DB_CONFIG = {
    'host': os.environ.get('GIS_DB_HOST', 'gisdb.systra.info'),
    'port': os.environ.get('GIS_DB_PORT', '5432'),
    'dbname': os.environ.get('GIS_DB_NAME', 'uk_irl'),
    'user': os.environ.get('GIS_DB_USER', ''),
    'password': os.environ.get('GIS_DB_PASSWORD', ''),
    'sslmode': os.environ.get('GIS_DB_SSLMODE', 'require'),
}

MINIO_ENDPOINT = os.environ.get('MINIO_ENDPOINT', 'http://gisdb.systra.info:9000')
MINIO_ACCESS_KEY = os.environ.get('MINIO_ACCESS_KEY', '')
MINIO_SECRET_KEY = os.environ.get('MINIO_SECRET_KEY', '')