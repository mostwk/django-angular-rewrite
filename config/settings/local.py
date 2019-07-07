from .base import *  # noqa
from .base import env

# GENERAL
DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="rY60XSL9i8MveamJaWIcG7QLtGd7XvERZlDIA1tEJBZrHY3rb8cUvNrtAvxXycqF",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# CACHES

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# TEMPLATES

TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # noqa F405

# EMAIL

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"  # noqa
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]  # noqa

# Celery

CELERY_TASK_EAGER_PROPAGATES = True
