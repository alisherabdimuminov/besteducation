from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class UserCreateModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


class UserUpdateModelForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")