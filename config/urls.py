from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^api/', include('django_rewrite.apis.urls', namespace='api')),
]
