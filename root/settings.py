"""
Django settings for root project.

Generated by 'django-admin startproject' using Django 5.0.7.
"""

import os
import environ
from pathlib import Path

env = environ.Env(DEBUG=(bool, True))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bk73v93gase@p7uq2r0*4aq&axlf-bbi9k3tp1x_x28=nzsx2('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs.apps.BlogsConfig',
    'courses.apps.CoursesConfig',
    'teachers.apps.TeachersConfig'
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

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'root.wsgi.application'

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env('NAME'),
        "USER": env('USER'),
        "PASSWORD": env('PASSWORD'),
        "HOST": env('HOST'),
        "PORT": env('PORT'),
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'courses.User'

JAZZMIN_SETTINGS = {
    'site_title': 'Online Course',
    'site_header': 'E-Platform',
    'site_brand': 'WWW',
    'site_logo': 'https://media.emailonacid.com/wp-content/uploads/2018/06/HC-GettingStarted.png',
    'welcome_sign': 'Welcome to the Admin Area',
    'copyright': 'Najot Ta\'lim',
    'search_model': 'auth.User',
    'user_avatar': 'https://media.emailonacid.com/wp-content/uploads/2018/06/HC-GettingStarted.png',

    # Top Menu #
    'topmenu_links': [
        {'name': 'Home', 'url': 'admin:index', 'permissions': ['auth.view_user']},
        {'name': 'Support', 'url': 'https://support.example.com', 'new_window': True},
    ],

    # Side Menu #
    'show_sidebar': True,

    'navigation_expanded': True,

    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },

    # Relative paths to custom CSS/JS files
    'custom_css': 'css/admin_custom.css',
    'custom_js': 'js/admin_custom.js',

    'show_ui_builder': True,
}
