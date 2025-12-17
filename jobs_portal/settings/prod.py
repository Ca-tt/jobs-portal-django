from .base import *

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["damir96.pythonanywhere.com","www.damir96.pythonanywhere.com"]
)


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

CSRF_TRUSTED_ORIGINS = env.list('ALLOWED_HOSTS', default=["https://damir96.pythonanywhere.com","http://www.damir96.pythonanywhere.com"])

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"




