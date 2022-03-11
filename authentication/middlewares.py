import jwt
from django.utils.deprecation import MiddlewareMixin
from jwt import DecodeError

from backend.settings import SECRET_KEY

from django.contrib.auth.models import AnonymousUser


class AuthenticationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        token = request.COOKIES.get("token")
        try:
            request.user = jwt.decode(token, SECRET_KEY, algorithms=["H256"])

        except DecodeError:
            request.user = AnonymousUser()


