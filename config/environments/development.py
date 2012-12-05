from path import path
from config.settings import *
import sys

sys.dont_write_bytecode = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT / 'db/development.sqlite3',
    }
}

DEBUG = True

# config/environments/local.py is ignored to allow for easy settings
# overrides without affecting others environments / developers
try:
    from local import *
except ImportError:
    pass
