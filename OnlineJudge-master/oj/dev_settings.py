# coding=utf-8
import os
from utils.shortcuts import get_env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = f"{BASE_DIR}/data"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env('POSTGRES_HOST', 'YOUR_POSTGRES_HOST'),
        'PORT': get_env('POSTGRES_PORT', '5432'),
        'NAME': get_env('POSTGRES_DB', 'onlinejudge'),
        'USER': get_env('POSTGRES_USER', 'onlinejudge'),
        'PASSWORD': get_env('POSTGRES_PASSWORD', 'onlinejudge')
    }
}

REDIS_CONF = {
    'host': get_env('REDIS_HOST', 'YOUR_REDIS_HOST'),
    'port': get_env('REDIS_PORT', '6379'),
    'password': get_env('REDIS_PASSWORD', 'YOUR_REDIS_PASSWORD')
}


DEBUG = True

ALLOWED_HOSTS = ["*"]


