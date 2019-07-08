from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from django_rewrite.users.forms import UserChangeForm, UserCreationForm
from .models import User, Profile


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["username", "is_superuser"]
    search_fields = ["username"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'avatar']
