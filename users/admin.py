from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserCreateModelForm, UserUpdateModelForm


@admin.register(User)
class UserModelAdmin(UserAdmin):
    add_form = UserCreateModelForm
    form = UserUpdateModelForm
    model = User

    add_fieldsets = (
        ("Yangi foydalanuvchi qo'shish", {
            "fields": ("username", "first_name", "last_name", "is_student")
        })
    )
    fieldsets = (
        ("Foydalanuvchini tahrirlash", {
            "fields": ("username", "first_name", "last_name", "is_payed", "last_pay_date", "is_student")
        }),
    )

    list_display = ["username", "first_name", "last_name", "is_payed", "last_pay_date"]
