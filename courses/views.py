from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import (
    Course,
    Question,
    Quiz,
    Answer,
    Lesson
)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def courses(request):
    courses = Course.objects.all()
    c = []
    for course in courses:
        c.append({
            "id": course.pk,
            "name": course.name,
            "subject": course.subject.name,
            "author": {
                "first_name": course.author.first_name,
                "last_name": course.author.last_name
            },
            "description": course.description,
            "feedback": course.feedback,
            "price": course.price,
            "count_lessons": course.count_lessons(),
            "count_quizzes": course.count_quizzes(),
            "created_at": course.created_at,
        })
    return Response(c)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def course(request, pk):
    course = None
    try:
        course = Course.objects.get(pk=pk)
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "course not found"
        })
    lessons = []
    counter = 0
    for lesson in course.lessons().all():
        lessons.append({
            "id": lesson.pk,
            "number": counter,
            "lesson": lesson.name,
        })
        counter += 1
    return Response({
        "id": course.pk,
        "name": course.name,
        "subject": course.subject.name,
        "author": {
            "first_name": course.author.first_name,
            "last_name": course.author.last_name
        },
        "description": course.description,
        "feedback": course.feedback,
        "price": course.price,
        "count_lessons": course.count_lessons(),
        "count_quizzes": course.count_quizzes(),
        "lessons": lessons,
        "created_at": course.created_at,
    })

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def lesson(request, course_id, lesson_id):
    course = None
    lesson = None
    try:
        course = Course.objects.get(pk=course_id)
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "course not found"
        })
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "lesson not found"
        })
    if lesson.quiz:
        quiz = {
            "name": lesson.quiz.name,
            "questions": [{"question": q.question, "type": q.type, "answers": [{"value": a.value, "is_correct": a.is_correct} for a in q.answers.all()]} for q in lesson.quiz.questions.all()]
        }
    else:
        quiz = {}
    previous = lesson.previous
    if previous:
        previous = {
            "id": previous.pk,
            "name": previous.name,
        }
    else:
        previous = {}
    next = lesson.next
    if next:
        next = {
            "id": next.pk,
            "name": next.name,
        }
    else:
        next = {}
    
    if lesson.previous:
        if request.user in lesson.finishers.all():
            return Response({
                "name": lesson.name,
                "video": lesson.video,
                "resource": lesson.resource,
                "type": lesson.type,
                "quiz": quiz,
                "previous": previous,
                "next": next
            })
        else:
            return Response({
                "status": "error",
                "message": "oldingi dars tamomlanmagan"
            })
    print({
        "name": lesson.name,
        "video": lesson.video,
        "resource": lesson.resource.url,
        "type": lesson.type,
        "quiz": quiz,
        "previous": previous,
        "next": next,
    })
    return Response({
        "name": lesson.name,
        "video": lesson.video,
        "resource": lesson.resource.url,
        "type": lesson.type,
        "quiz": quiz,
        "previous": previous,
        "next": next,
    })

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def feedback(request, course_id):
    user = request.user
    feed = request.data.get("feed")
    course = None
    try:
        course = Course.objects.get(pk=course_id)
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "course not found"
        })
    try:
        feed = int(feed)
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "feed must be integer"
        })
    course_feedbackers = course.feedbackers.count()
    courese_feedback = course.feedback
    course.feedback = (courese_feedback + feed) / course_feedbackers
    course.save()
    return Response({
        "status": "ok",
        "message": "successfuly feedbacked"
    })
