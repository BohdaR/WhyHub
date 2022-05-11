from .defaults import *


SECRET_KEY = "fghdfgiohbfgsujpb9sfdgoijbrsf9pbiojsfdgbbfifgofdg5654645"

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}