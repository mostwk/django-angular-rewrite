from django.conf.urls import include, url

urlpatterns = [
    url(
        regex='^auth/',
        view=include('django_rewrite.authentication.urls', namespace='auth')
    )
]