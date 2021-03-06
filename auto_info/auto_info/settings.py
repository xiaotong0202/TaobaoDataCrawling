"""
Django settings for auto_info project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import uuid

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zuf0blcwlnni+n#h_zm_egu)c-(60xo-ocnu5id%!1tzgnqo(9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

RUN_ENV = os.getenv("RUN_ENV")
MYSQL_NAME = os.getenv("MYSQL_NAME")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_IP = os.getenv("MYSQL_IP")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
LOGIN_METHOD = os.getenv("LOGIN_METHOD", 'driver')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'df_info'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'auto_info.urls'

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

WSGI_APPLICATION = 'auto_info.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if RUN_ENV == "local":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'crawl_info_server',
            'USER': 'root',
            'PASSWORD': 'mysql',
            'HOST': 'localhost',
            'PORT': 3306,
        }
    }

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '{}'.format(MYSQL_NAME),
            'USER': '{}'.format(MYSQL_USER),
            'PASSWORD': '{}'.format(MYSQL_PASSWORD),
            'HOST': '{}'.format(MYSQL_IP),
            'PORT': int(MYSQL_PORT),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# DETAIL CONFIGURATION
MOUSE_MOVE_INTERVAL_MEAN = os.environ.get('MOUSE_MOVE_INTERVAL_MEAN', 0.018)
MOUSE_MOVE_INTERVAL_SIGMA = os.environ.get('MOUSE_MOVE_INTERVAL_SIGMA', 0.001)
MOUSE_MOVE_SPEED_MEAN = os.environ.get('MOUSE_MOVE_SPEED_MEAN', 600)
MOUSE_MOVE_SPEED_SIGMA = os.environ.get('MOUSE_MOVE_SPEED_SIGMA', 50)

# LOGIN CONFIGURATION
SITE_API_TIMEOUT = 300

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)-8s %(message)s'
        },
        'detail': {
            'format': '%(asctime)s %(levelname)-8s %(pathname)s[line:%(lineno)d] %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "log_path", 'debug.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 10,
            'formatter': 'detail',
        },

    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

#  chromedriver路径
CHROMEDRIVER = "/usr/local/bin/chromedriver"

#  kafka的ip与port
KAFKA_IP = os.getenv("KAFKA_IP")
KAFKA_PORT = os.getenv("KAFKA_PORT")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# redis的ip与port
REDIS_IP = os.getenv("REDIS_IP")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

#  30天换成miao
DEADLINE_TIME = 30 * 24 * 3600

# 限制请求次数
SERVER_ID_FORBIDDEN_COUNT = 4
SERVER_RANDOM_UUID = str(uuid.uuid4()) + '_chrome_queue'

WARNING_SERVER_NAME = os.getenv("WARNING_SERVER_NAME")
CONSUL_HOST = os.getenv("CONSUL_HOST")
CONSUL_PORT = os.getenv("CONSUL_PORT")
CONSUL_PROXY = {'http': 'http://106.14.225.40:31080',
                'https': 'https://106.14.225.40:31080'}
DING_DING_SEND_API = 'http://{}/warning/?service_id={}&warning_level={}&warning_content={}'
