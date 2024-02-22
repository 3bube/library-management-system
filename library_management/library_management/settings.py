"""
Django settings for library_management project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4!j1dleel3n7x_u_fk_-rrf8vjk!f6i&q-jmsb1s#ts^)(eebl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',               # Django Admin
    'django.contrib.auth',                # Django Authentication System
    'django.contrib.contenttypes',        # Django content types framework
    'django.contrib.sessions',            # Django session framework
    'django.contrib.messages',            # Django messaging framework
    'django.contrib.staticfiles',         # Django static file serving
    'books.apps.BooksConfig',             # Custom 'books' app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # Django security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Django session middleware
    'django.middleware.common.CommonMiddleware',             # Django common middleware
    'django.middleware.csrf.CsrfViewMiddleware',             # Django CSRF middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Django authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',     # Django messaging middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Django X-Frame-Options middleware
]

ROOT_URLCONF = 'library_management.urls'    # Root URL configuration

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],    # Template directories
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

WSGI_APPLICATION = 'library_management.wsgi.application'    # WSGI application entry point

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # Use sqlite3 for development
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),    # SQLite database file path
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),    # Additional static file directories
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'    # Default primary key field type