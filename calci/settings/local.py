from .base import *

SECRET_KEY = '_=z4rr&th#7w5bbpz&wt9d&7=8ul$lhwhztl0sxeqk1^ub)z)$'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# SwampDragon settings
SWAMP_DRAGON_CONNECTION = ('swampdragon.connections.sockjs_connection.DjangoSubscriberConnection', '/data')
DRAGON_URL = 'http://127.0.0.1:9999'
SWAMP_DRAGON_REDIS_HOST = '127.0.0.1'
SWAMP_DRAGON_REDIS_PORT = 6379
