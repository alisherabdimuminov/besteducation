from django.forms import ModelForm

from .models import Lesson

class LessonCreateModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ("course", "name", "video", "resource", "quiz", "type", "previous", "next")

class LessonUpdateModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ("course", "name", "video", "resource", "quiz", "type", "previous", "next")
