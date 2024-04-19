from django.db import models

from users.models import User


LESSON_TYPE = (
    ("lesson", "Lesson"),
    ("quiz", "quiz")
)

QUESTION_TYPE = (
    ("one_select", "One select"),
    ("multi_select", "Multi select"),
    ("writeable", "Writeable")
)

class Answer(models.Model):
    value = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.value

class Question(models.Model):
    question = models.TextField()
    answers = models.ManyToManyField(Answer, related_name="question_answers")
    type = models.CharField(max_length=20, choices=QUESTION_TYPE)

    def __str__(self):
        return self.question


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question, related_name="quiz_questions")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name="course_subject")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="course_author")
    description = models.TextField(null=True, default="")
    feedback = models.FloatField(null=True, default=0)
    feedbackers = models.ManyToManyField(User, related_name="course_feedbackers", null=True, blank=True)
    price = models.IntegerField(null=True, default=0)
    students = models.ManyToManyField(User, related_name="course_students", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def count_lessons(self):
        lessons = Lesson.objects.filter(course=self, type="lesson")
        return lessons.count()
    
    def count_quizzes(self):
        quizzes = Lesson.objects.filter(course=self, type="quiz")
        return quizzes.count()
    
    def lessons(self):
        return Lesson.objects.filter(course=self)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lesson_course")
    name = models.CharField(max_length=200)
    video = models.URLField(max_length=500)
    resource = models.FileField(upload_to="lessons/", null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True, related_name="lesson_quiz", blank=True)
    type = models.CharField(max_length=20, choices=LESSON_TYPE)
    previous = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="previous_lesson")
    next = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="next_name")
    finishers = models.ManyToManyField(User, related_name="lesson_finishers", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name + " - " + self.name
