from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myapp_db',
        'USER': 'www',
        'PASSWORD': 'testpassword',
        'HOST': '127.0.0.1',
    },
}
