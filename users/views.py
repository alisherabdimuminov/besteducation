from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import User

@api_view(http_method_names=["POST"])
def login(request):
    username = request.data.get("phone")
    password = request.data.get("password")
    user = None
    try:
        user = User.objects.filter(username=username).first()
        check_password = user.check_password(password)
        if not check_password:
            return Response({
                "status": "error",
                "message": "password not valid"
            })
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "phone number is not defined"
        })
    token = None
    try:
        token = Token.objects.get_or_create(user=user)
        token[0].delete()
        token = Token.objects.create(user=user)
        print(token)
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "Token not found"
        })
    return Response({
        "token": str(token)
    })

@api_view(http_method_names=["POST"])
def signup(request):
    username = request.data.get("phone")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    password = request.data.get("password")
    try:
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return Response({
            "status": "ok",
            "message": "Account created successfuly"
        })
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "phone number already exists"
        })
    
@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def students(request):
    users_obj = User.objects.filter(is_student=True)
    users = []
    for user in users_obj:
        users.append({
            "id": user.pk,
            "phone": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_payed": user.is_payed,
            "last_pay_date": user.last_pay_date
        })
    return Response(users)

@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def teachers(request):
    users_obj = User.objects.filter(is_student=False)
    users = []
    for user in users_obj:
        users.append({
            "id": user.pk,
            "phone": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name
        })
    return Response(users)

@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def student(request, phone):
    user = None
    try:
        user = User.objects.filter(username=phone, is_student=True).first()
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "student not found"
        })
    if user:
        return Response({
            "id": user.pk,
            "phone": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_payed": user.is_payed,
            "last_pay_date": user.last_pay_date
        })
    else:
        return Response({
            "status": "error",
            "message": "student not found"
        })

@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def teacher(request, phone):
    user = None
    try:
        user = User.objects.filter(username=phone, is_student=False).first()
    except Exception as e:
        print(e)
        return Response({
            "status": "error",
            "message": "teacher not found"
        })
    if user:
        return Response({
            "id": user.pk,
            "phone": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name
        })
    else:
        return Response({
            "status": "error",
            "message": "teacher is not found"
        })
