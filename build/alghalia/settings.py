import os


gettext_noop = lambda s: s


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Taylan Pince', 'taylanpince@gmail.com'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'no-reply@alghalia.net'

SITE_ID = 1

USE_I18N = True

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('ar', gettext_noop('Arabic')),
    ('en', gettext_noop('English')),
)

SECRET_KEY = 'dc*zakji7&t*yz7=mv)ak*rqp17m&oa6w_-pc(ia&d14(il8b9'

TIME_ZONE = 'Canada/Eastern'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'comments.context_processors.comment_cookies',
    'sharer.context_processors.share_uri',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'batchadmin',
    'captcha',
    'django_extensions',
    'sharer',
    'south',
    'tagging',
    
    'articles',
    'comments',
)

CAPTCHA_FONT_SIZE = 32
CAPTCHA_FONT_PATH = os.path.join(MEDIA_ROOT, 'fonts/georgia-bold.ttf')

try:
    from settings_local import *
except ImportError:
    pass
