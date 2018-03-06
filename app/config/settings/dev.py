from .base import *

DEBUG = True

secrets = json.loads(open(SECRETS_DEV, 'rt').read())
ALLOWED_HOSTS = []
DATABASES = secrets['DATABASES']
