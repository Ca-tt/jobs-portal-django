from .base import *

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


