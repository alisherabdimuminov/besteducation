from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import (
    Course,
    Lesson,
    Quiz,
    Question,
    Answer,
    Subject
)
from .forms import (
    LessonCreateModelForm,
    LessonUpdateModelForm
)

@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "count_lessons", "count_quizzes"]

@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    add_form = LessonCreateModelForm
    form = LessonUpdateModelForm

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        print(request.GET)
        return super().get_queryset(request)
    

@admin.register(Quiz)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["name"]    

@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["question"]

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ["value", "is_correct"]

@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
