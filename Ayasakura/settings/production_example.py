import os


def envbool(s, default):
    v = os.getenv(s, default=default)
    if v not in ("", "True", "False"):
        msg = "Unexpected value %s=%s, use 'True' or 'False'" % (s, v)
        raise Exception(msg)
    return v == "True"


def envint(s, default):
    v = os.getenv(s, default)
    if v == "None":
        return None
    return int(v)


MASTER_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR        = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR    = os.path.join(os.path.dirname(MASTER_BASE_DIR),'templates')
SECRET_KEY      = os.getenv('SECRET_KEY','8yh_$^g$woalti1297(kypznlodb&6ggdkexj9g$xdh+ox+=%&')

ALLOWED_HOSTS               = ['localhost','127.0.0.1']
DEBUG_PROPAGATE_EXCEPTIONS  = envbool('DEBUG_PROPAGATE_EXCEPTIONS', 'False')
DEBUG                       = envbool('DEBUG', 'False')
CORS_ORIGIN_ALLOW_ALL       = envbool('CORS_ORIGIN_ALLOW_ALL', 'True')
CORS_ALLOW_CREDENTIALS      = envbool('CORS_ALLOW_CREDENTIALS', 'True')

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8002', 
    'http://localhost:8000'   
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

INSTALLED_APPS = [
    'jet-dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'rest_framework',
    'easyaudit',
    'allauth',
    'allauth.account',   
    'des' ,
]

MIDDLEWARE = [
    # 'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

DATABASES = {    
    'default': {
       'ENGINE': 'django.db.backends.mysql',
        'USER': 'dummyuser',
        'PASSWORD': 'dummypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'dummydb'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

STATICFILES_DIRS = [   
    os.path.join(BASE_DIR, 'assets/statics'),
]

CRISPY_TEMPLATE_PACK            = 'bootstrap4'
MESSAGE_STORAGE                 = 'django.contrib.messages.storage.cookie.CookieStorage'
STATICFILES_STORAGE             = 'django.contrib.staticfiles.storage.StaticFilesStorage'
EMAIL_BACKEND                   = 'des.backends.ConfiguredEmailBackend'

ROOT_URLCONF                    = 'Ara.urls'
WSGI_APPLICATION                = 'Ara.wsgi.application'
LANGUAGE_CODE                   = 'en-us'
TIME_ZONE                       = 'Asia/Jakarta'
ACCOUNT_AUTHENTICATION_METHOD   = 'username_email'
X_FRAME_OPTIONS                 = 'DENY'
CSRF_COOKIE_SECURE              = True
SECURE_CONTENT_TYPE_NOSNIFF     = True
SECURE_BROWSER_XSS_FILTER       = True
SESSION_COOKIE_SECURE           = True
IMPORT_EXPORT_USE_TRANSACTIONS  = True
ACCOUNT_EMAIL_REQUIRED          = True
USE_I18N                        = True
USE_L10N                        = True
USE_TZ                          = True

STATIC_ROOT                     = '/assets/statics/'
MEDIA_ROOT                      = '/assets/media/'
STATIC_URL                      = '/static/'
MEDIA_URL                       = '/media/'
LOGIN_URL                       = '/account/login/'
LOGOUT_URL                      = '/account/logout/'
LOGOUT_REDIRECT_URL             = '/'
LOGIN_REDIRECT_URL              = '/'