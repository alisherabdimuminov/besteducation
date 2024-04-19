from django.urls import path

from .views import (
    courses,
    course,
    lesson,
)

urlpatterns = [
    path("", courses, name="courses"),
    path("course/<int:pk>/", course, name="course"),
    path("course/<int:course_id>/lesson/<int:lesson_id>/", lesson, name="lesson"),
]
