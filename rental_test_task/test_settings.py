from .settings import *


DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

DEBUG = False
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "local.rental_test_task.co"]

SECURE_SSL_REDIRECT = False

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

ENABLE_DOGSTATS = False
