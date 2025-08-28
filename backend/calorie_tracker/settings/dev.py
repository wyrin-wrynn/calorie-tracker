from .base import *  # noqa: F403,F401

DEBUG = True
ALLOWED_HOSTS = ["192.168.1.30", "localhost", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["http://192.168.1.30:8000"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "calories",
        "USER": "calorie",
        "PASSWORD": "calorie",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
