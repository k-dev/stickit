from settings import *
import shutil

shutil.copyfile('db-template.sqlite', 'db-test.sqlite')

DATABASES = {
    'default': {
        'NAME': 'db-test.sqlite',
        'ENGINE': 'django.db.backends.sqlite3'
    },
}