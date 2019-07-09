from django.conf.urls import url

from django_rewrite.authentication import apis

app_name = 'authentication'

urlpatterns = [
    url(
        regex='^login/$',
        view=apis.LoginApi.as_view(),
        name='login'
    ),
    url(
        regex='^register/$',
        view=apis.RegistrationApi.as_view(),
        name='register'
    ),
    url(
        regex='^me/$',
        view=apis.UserDetailApi.as_view(),
        name='user-detail'
    ),
    url(
        regex='^me/profile/$',
        view=apis.UserProfileApi.as_view(),
        name='user-profile'
    ),
]
