from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5^u!$kk4$ky^)t-toa!x#u*-#pitl7h-+_0tpf8e*b$gsy#!wo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_apscheduler',
    
    'django_filters',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'sign',
    'protect',
    'news.apps.NewsConfig',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    
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
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]



WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = '/static/'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/news/'

SITE_ID = 1

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False 
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'имя_почты'
EMAIL_HOST_PASSWORD = 'пароль_от_приложения'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'Ваша_почта'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

#Логгирование в django
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'regular_console': {
            'format': '[%(asctime)s] %(levelname)-7s %(message)s'
        },
        'warning_console': {
            'format': '[%(asctime)s] %(levelname)-7s %(message)s %(pathname)s'
        },
        'error': {
            'format': '[%(asctime)s] %(levelname)-7s %(message)s %(pathname)s %(exc_info)s'
        },
        'general_log': {
            'format': '[%(asctime)s] %(levelname)-7s %(module)s: %(message)s'
        },
        'email': {
            'format': '[%(asctime)s] %(levelname)-7s %(message)s %(pathname)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'regular_console',
        },
        'warning_handler': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_console',
        },
        'error_handler': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error',
        },
        'general_log_handler': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'general_log',
            "filename": f"{BASE_DIR}/log_files/general.log",
        },
        'error_file_handler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'error',
            "filename": f"{BASE_DIR}/log_files/errors.log",
        },
        'security_file_handler': {
            'level': 'INFO',
            'formatter': 'general_log',
            'class': 'logging.FileHandler',
            "filename": f"{BASE_DIR}/log_files/security.log",
        },
        'mail_admin': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'warning_console',
            'filters': ['require_debug_false'],
            "email_backend": "django.core.mail.backends.filebased.EmailBackend",
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'warning_handler', 'general_log_handler', 'error_handler'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['error_file_handler', 'mail_admin'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['error_file_handler'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['error_file_handler', 'mail_admin'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db_backend': {
            'handlers': ['error_file_handler'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security_file_handler'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

