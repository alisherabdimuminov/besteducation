from django.urls import path
from .views import (
    signup, 
    login,
    students,
    teachers,
    student,
    teacher
    )


urlpatterns = [
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("students/", students, name="students"),
    path("student/<str:phone>/", student, name="student"),
    path("teachers/", teachers, name="teachers"),
    path("teacher/<str:phone>/", teacher, name="teacher"),
]
