from django.urls import path

from authentication.api import sign_up, sign_in

urlpatterns = [
    path("auth/signup", sign_up),
    path("auth/signin", sign_in)


]
