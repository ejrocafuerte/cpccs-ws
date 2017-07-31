"""
Django settings for cpccsapi project.

Generated by 'django-admin startproject' using Django 1.10.6.

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
SECRET_KEY = '+sx1%al*!4@^f6pbeo_a1ygw@zl9m3ui*8kd=_b9orfgk0s8)f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = True

ALLOWED_HOSTS = [
	#'.6v3gjmadmw.sa-east-1.elasticbeanstalk.com'
	#'localhost',
	#'127.0.0.1',
	'ejrocafuerte.pythonanywhere.com',
]


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Django REST Framework
	'rest_framework',
	# CPCCS application
	'cpccs.apps.CpccsConfig',
	# Crispy forms
	'crispy_forms',
	#Django Filters
	'django_filters',
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

ROOT_URLCONF = 'cpccsapi.urls'

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

WSGI_APPLICATION = 'cpccsapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
#'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'cpccsdb',
#        'USER': 'root',
#        'PASSWORD': 'rubik',
#        'HOST': 'localhost',
#    }
#'default': {
#'ENGINE': 'django.db.backends.postgresql',
#		'OPTIONS' : {
#		#'options': '-c search_path=cpccs'
#		'options': '-c search_path=public'
#		},
#		'NAME': 'cpccsDB',
#		'USER': 'postgres',
#		'PASSWORD':'root',
#		'HOST': 'localhost',
#		'PORT': '5432',
#	}
	#'default': {
		#'ENGINE': 'django.db.backends.postgresql',
	#    'ENGINE': 'django.db.backends.mysql',
	#	'OPTIONS' : {
	 #           'options': '-c search_path=cpccs'
	  #   },
		# Replace games with your desired database name
		#'NAME': 'omkbmadd',
	   # 'NAME':'cpccsDB',
		# Replace username with your desired user name
		#'USER': 'omkbmadd',
		#'USER':'ejrocafuerte',
		# Replace password with your desired password
		#'PASSWORD': 'jK72m7jV5797WwXGbFX9CV0p86-gBU4x',
		#'PASSWORD':'NyZjeXDQFcUC4xiaC_WXrF9yKXA-1gH9',
		# Replace 127.0.0.1 with the PostgreSQL host
		#'HOST': 'babar.elephantsql.com',
		#'HOST':'ejrocafuerte.mysql.pythonanywhere-services.com',
		# Replace 5432 with the PostgreSQL configured port
		# in case you aren't using the default port
		#'PORT': '3306',
	#}
	'default': {
		'OPTIONS':{
	        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
	        },
	    'ENGINE': 'django.db.backends.mysql',
	    'NAME': 'ejrocafuerte$default',
	    'USER': 'ejrocafuerte',
		'PASSWORD': 'Irisluciana01',
		'HOST': 'ejrocafuerte.mysql.pythonanywhere-services.com',
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
# https://docs.djangoproject.com/en/1.10/topicomcs/i18n/

LANGUAGE_CODE = 'es-ec'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject./en/1.10/howto/static-files/
STATIC_ROOT = '/cpccs-ws/cpccsapi/static/'
STATIC_URL = '/static/'

REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS':
	'cpccs.pagination.LimitOffsetPaginationWithMaxLimit',
	'PAGE_SIZE': 10,
	'DEFAULT_FILTER_BACKENDS': (
		'rest_framework.filters.DjangoFilterBackend',
		'rest_framework.filters.SearchFilter',
		'rest_framework.filters.OrderingFilter',
		),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
		),
	#'DEFAULT_PERMISSION_CLASSES': (
	#    'rest_framework.permissions.IsAuthenticated',
	#)
}