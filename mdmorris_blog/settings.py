"""
Django settings for mdmorris_blog project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q3hyc$+gx3cf3p%10crgzs$&8zx__a0cwwr@k%k+zr)56+xkhs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'django.contrib.sitemaps',
    'django_comments',
    'mptt',
    'tagging',
    'my_zinnia_bootstrap',
    'zinnia_gallery.apps.ZinniaGalleryConfig',
#    'zinnia_gallery',
    'zinnia',
    'django_xmlrpc',
    'disqus',
    'photologue',
    'sortedm2m',
    'photologue_custom',
    'ckeditor',
    'taggit',
    'frontpage.apps.FrontpageConfig',
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

ROOT_URLCONF = 'mdmorris_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'zinnia_gallery/templates')],
        'APP_DIRS': False,
        'OPTIONS': {
	    'loaders':[
		'app_namespace.Loader',
		'django.template.loaders.app_directories.Loader',
		],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
		'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
		'zinnia.context_processors.version',
            ],
        },
    },
]

WSGI_APPLICATION = 'mdmorris_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, '../database/db.sqlite3'),
#    }
#}

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'mdmorris',
		'USER':'mark',
		'PASSWORD':'04sirroMDM13',
		'HOST':'localhost',
		'PORT':'',
	}
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en'



TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../media')) 
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../static'))


#STATICFILES_DIRS = [BASE_DIR,]
#STATIC_ROOT = os.path.join(BASE_DIR, 'uploads')

SITE_ID = 1

#Zinnia settings:
MIGRATION_MODULES = {'zinnia': 'zinnia_gallery.migrations_zinnia'}
ZINNIA_ENTRY_BASE_MODEL = 'zinnia_gallery.models.EntryGallery'
#ZINNIA_ENTRY_CONTENT_TEMPLATES = 'zinnia/_entry_detail.html'
ZINNIA_ENTRY_CONTENT_TEMPLATES = [
		('zinnia/_entry_detail.html', 'just Disqus comments'),
		]
ZINNIA_ENTRY_DETAIL_TEMPLATES = [
		('zinnia/entry_detail.html', 'just Disqus comments'),
		]

#Disqus settings:
DISQUS_API_KEY = 'QX2j26a39IIJoq1RzljpnhmzMHuXGjH5I4LtpIP5MUD2vaLQnysXbvbvPwF4HJaP'
DISQUS_WEBSITE_SHORTNAME = 'www-mdmorris-co-uk'
