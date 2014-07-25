# Django settings for hms project.
import os 
from django.core.mail import send_mail

SITE_ROOT = os.path.join(os.path.dirname(__file__), '..') 

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Pulkit Pahwa', 'pulkitpahwa11@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'home',                      
        'USER': 'home',
        'PASSWORD': 'home',
        'HOST': 'localhost',                 
        'PORT': '5432', 
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Kolkata'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media') 
MEDIA_URL = '/media/' 
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = ( 
    os.path.join(SITE_ROOT, 'staticfiles') ,
) 

TEMPLATE_DIRS = ( 
    os.path.join(SITE_ROOT, 'templates') ,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = ')o)$7!ts-9&ibqn9g53ppn++*tij-nidt7gbz3e8w_e6*upuo3'

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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hms.urls'

WSGI_APPLICATION = 'hms.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'guardian',
    'widget_tweaks',
    'braces',
    'profiles',
    'attendance',
    'outpas',
    'msg',
)
LOGIN_URL = '/login/'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


ANONYMOUS_USER_ID = -1
GUARDIAN_RENDER_403 = True

try : 
    from email_settings import *
except :
    from local_settings import *
