import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
