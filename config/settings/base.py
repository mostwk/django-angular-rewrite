"""
Base settings to build other settings files upon.
"""

import environ

ROOT_DIR = (
    environ.Path(__file__) - 3
)  # (django_rewrite/config/settings/base.py - 3 = django_rewrite/)
APPS_DIR = ROOT_DIR.path("django_rewrite")

env = environ.Env()

env.read_env(str(ROOT_DIR.path(".env")))

# GENERAL
DEBUG = env.bool("DJANGO_DEBUG", False)

TIME_ZONE = "Europe/Moscow"

LANGUAGE_CODE = "en-us"

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [ROOT_DIR.path("locale")]

# DATABASES

DATABASES = {"default": env.db("DATABASE_URL")}

DATABASES["default"]["ATOMIC_REQUESTS"] = True

# URLS

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

# APPS
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "image_cropping",
    "django_extensions",
    # "django_celery_beat",
]

LOCAL_APPS = [
    "django_rewrite.users",
    "django_rewrite.apis",
    "django_rewrite.authentication",
    "django_rewrite.common",
    "django_rewrite.posts",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS

MIGRATION_MODULES = {"sites": "django_rewrite.contrib.sites.migrations"}

# AUTHENTICATION

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "users.User"

# PASSWORDS

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},  # noqa
]

# MIDDLEWARE

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC

STATIC_ROOT = str(ROOT_DIR("staticfiles"))

STATIC_URL = "/static/"

STATICFILES_DIRS = [str(APPS_DIR.path("static"))]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA

MEDIA_ROOT = str(APPS_DIR("media"))

MEDIA_URL = "/media/"

# TEMPLATES

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR.path("templates"))],
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

CRISPY_TEMPLATE_PACK = "bootstrap4"


# SECURITY

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = "DENY"

# EMAIL

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"  # noqa
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',  # noqa
    'PAGE_SIZE': 10,

}
# ADMIN

ADMIN_URL = "admin/"

ADMINS = [("""mostwk""", "moskvichev.95@gmail.com")]

MANAGERS = ADMINS

# LOGGING

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Celery
# if USE_TZ:
#     CELERY_TIMEZONE = TIME_ZONE

# CELERY_BROKER_URL = env("CELERY_BROKER_URL")

# CELERY_RESULT_BACKEND = CELERY_BROKER_URL

# CELERY_ACCEPT_CONTENT = ["json"]

# CELERY_TASK_SERIALIZER = "json"

# CELERY_RESULT_SERIALIZER = "json"

# CELERY_TASK_TIME_LIMIT = 5 * 60

# CELERY_TASK_SOFT_TIME_LIMIT = 60

# CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
