from django.conf.urls import include, url

app_name = 'apis'

urlpatterns = [
    url('^auth/', include(
        'django_rewrite.authentication.urls', namespace='auth')),
]
