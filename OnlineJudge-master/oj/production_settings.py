from utils.shortcuts import get_env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env("POSTGRES_HOST", "oj-postgres"),
        'PORT': get_env("POSTGRES_PORT", "5432"),
        'NAME': get_env("POSTGRES_DB"),
        'USER': get_env("POSTGRES_USER"),
        'PASSWORD': get_env("POSTGRES_PASSWORD")
    }
}

REDIS_CONF = {
    'host': get_env('REDIS_HOST', 'YOUR_REDIS_HOST'),
    'port': get_env('REDIS_PORT', '6379'),
    'password': get_env('REDIS_PASSWORD', 'YOUR_REDIS_PASSWORD')
}

DEBUG = False

ALLOWED_HOSTS = ['*']

DATA_DIR = "/data"
