from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api', include('django_rewrite.apis.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
