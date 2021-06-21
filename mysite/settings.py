"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8ecv)oiqb76k3^_qgx68z_kx%1i5ead(v1fj!*$57r978p7cis'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'blog',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'uk-uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL='/media/'
STATIC_ROOT=os.path.join(BASE_DIR,'media')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID=1
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-',
'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy',
'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo',
'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace',
'-', 'SelectAll']},
            {'name': 'forms',
            'items': ['Form', 'Checkbox', 'Radio',
'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Itali', 'Underline',
'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
            'items': ['NumberedList', 'BulletedList', '-',
'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                        'JustifyLeft', 'JustifyCenter',
'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                        'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink',
'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table',
'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak',
'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format',
'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor',
'BGColor']},
            {'name': 'tools', 'items': ['Maximize',
'ShowBlock']},
            {'name': 'about', 'items': ['About']},
            '/', 

            {'name': 'yourcustomtools', 'items': [
               

                'Preview',
                'Maximize',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig', 
        'tabSpaces': 4,
        'extraPlugins': ','.join([
        'uploadimage', 
        'div',
        'autolink',
        'autoembed',
        'embedsemantic',
        'autogrow',
        'widget',
        'lineutils',
        'clipboard',
        'dialog',
        'dialogui',
        'elementspath'
        ]),
    }
}