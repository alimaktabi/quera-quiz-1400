from django.contrib.auth import authenticate
from django.http import JsonResponse

from authentication.forms import SignUpForm, LoginForm
from authentication.models import User

from backend.settings import SECRET_KEY

import jwt

bad_request_message = {"error": {"enMessage": "Bad Request!"}}


def create_successful_message(token: str):

    return {"message": "successful!", "token": token}


def encode_token(user):
    return jwt.encode({"email": user.email, "id": user.id}, SECRET_KEY, algorithm="HS256")


def sign_up(request):
    form = SignUpForm(data=request.POST)

    if not form.is_valid():
        return JsonResponse(bad_request_message, status=400)

    user = User(**form.cleaned_data)

    user.save()

    return JsonResponse(create_successful_message(encode_token(user)), status=200)


def sign_in(request):
    form = LoginForm(data=request.POST)

    if not form.is_valid():
        return JsonResponse(bad_request_message, status=400)

    # user = User.objects.filter(email__exact=form.cleaned_data.get("username")).first()
    user = authenticate(request, username=form.email, password=form.password)

    if user is None:
        return JsonResponse(bad_request_message, status=400)

    return JsonResponse(create_successful_message(encode_token(user)), status=200)


# def get_groups(request):
