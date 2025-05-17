from accounts.views.base import BaseView
from accounts.auth import Authentication
from accounts.serializers import UserSerializer

from rest_framework.response import Response

class Signup(BaseView):
    def post(self, request) -> None:
        # Implement the sign-up logic here
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        user = Authentication.signup(self, email=email, password=password, first_name=first_name, last_name=last_name)
        
        serializer = UserSerializer(user)

        return Response({
            "user": serializer.data,
        })