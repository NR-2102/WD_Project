"""
==============================================
 Django Settings for Kindle Clone Project
==============================================

This file contains the configuration settings for the Django project 
'kindle_clone'. It includes everything from database configurations 
to installed apps, middleware, static files, and more.

For more info on Django settings, visit:
https://docs.djangoproject.com/en/5.2/topics/settings/
"""

# ========== Import Path and OS Libraries ==========
from pathlib import Path
import os

# ========== Base Directory Path ==========
# This sets the base directory to the location of the current settings.py file.
BASE_DIR = Path(__file__).resolve().parent.parent


# ========== Quick-start Development Settings ==========
# These are the basic development settings for quick testing, not suitable for production.

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+*wab%v(pq*h!p*(z^&$r+dk0e^+a)r7p80xo93lf$_4tirot_'

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True  # Set to False in production

# Hosts that are allowed to connect to this Django project.
ALLOWED_HOSTS = []


# ========== Application Definition ==========
# Here we define the installed apps, middleware, templates, and WSGI configuration.

INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom app for handling books
    'books',
]

# List of middleware to handle requests and responses.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration for the project.
ROOT_URLCONF = 'kindle_clone.urls'

# Template settings to render HTML.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Can be populated with custom template directories.
        'APP_DIRS': True,  # Allows templates to be loaded from app directories.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application used for running the Django project.
WSGI_APPLICATION = 'kindle_clone.wsgi.application'


# ========== Database Configuration ==========
# Configure the database used by the project.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite used for development
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to the database file
    }
}


# ========== Password Validation ==========
# Password validation rules to enhance security.

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


# ========== Internationalization ==========
# Language and timezone settings for the project.

LANGUAGE_CODE = 'en-us'  # Language code for the project
TIME_ZONE = 'UTC'  # Timezone setting for the project

USE_I18N = True  # Enable internationalization
USE_TZ = True  # Enable timezone support


# ========== Static and Media Files ==========
# Configuration for serving static files (CSS, JS, images) and media files (uploads).

STATIC_URL = 'static/'  # URL path for static files

# Media files: where uploaded files are stored
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ========== Default Primary Key Field ==========
# Default field type for model primary keys (AutoField vs. BigAutoField).

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ========== Login and Logout Redirect URLs ==========
# Where users are redirected after logging in or logging out.

LOGIN_REDIRECT_URL = 'home'  # After login, users are redirected to the home page
LOGOUT_REDIRECT_URL = 'home'  # After logout, users are also redirected to the home page
