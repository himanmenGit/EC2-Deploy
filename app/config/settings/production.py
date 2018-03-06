from .base import *

DEBUG = False

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())
ALLOWED_HOSTS = [
    '.amazonaws.com',
]
DATABASES = secrets['DATABASES']
