from .base import *

DEBUG = True

secrets = json.loads(open(SECRETS_DEV, 'rt').read())
ALLOWED_HOSTS = []
DATABASES = secrets['DATABASES']

WSGI_APPLICATION = 'config.wsgi.dev.application'

# Media(User-uploaded files)를 위한 스토리지
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# Static files(collectstatic)를 위한 스토리지
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
