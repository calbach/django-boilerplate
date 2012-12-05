from config.settings import *
import dj_database_url

DATABASES = {
  'default': dj_database_url.config(default='postgres://localhost')
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# settings/local.py is ignored to allow for easy settings
# overrides without affecting others
try:
    from local import *
except ImportError:
    pass
