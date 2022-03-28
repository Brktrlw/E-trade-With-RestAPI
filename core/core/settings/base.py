import os
from datetime import timedelta
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    "ProductsApp",
    "UserApp",
    "CommentApp",
    "OrderApp",
    "CartApp",
    "FavoritesApp",
    "LikeApp",
    "SellerApp",
    #3rd Party Apps
    'django_cleanup',
    "phonenumber_field",
    "debug_toolbar",
    #"django.contrib.staticfiles",
    "django_celery_beat",
    "django_celery_results",
    "rest_framework",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF  = 'core.urls'

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
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
		'rest_framework.authentication.SessionAuthentication'
    ),

    'DEFAULT_THROTTLE_RATES': {
        'commentThrottle': '10/hour',
        "registerThrottle":"3/hour",
        "favoriteThrottle":"20/min",
        "sellerThrottle":"5/min"
    }

}

SIMPLE_JWT={
   'ACCESS_TOKEN_LIFETIME':timedelta(days=15)
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
AUTH_USER_MODEL = "UserApp.ModelUser"

INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_ROOT=os.path.join(BASE_DIR,"static_root")


LANGUAGES = [
    ('en', 'English'),
    ('tr', 'Turkish'),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale/')]

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE