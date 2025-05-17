from accounts.views.base import BaseView
from accounts.auth import Authentication
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class SignIn(BaseView):
    def post(self, request) -> None:
        # Implement the sign-in logic here
        email = request.data.get('email')
        password = request.data.get('password')

        user = Authentication.authenticate(self, email=email, password=password)
        
        token = RefreshToken.for_user(user)

        enterprise = self.get_enterprise_user(user.id)

        serializer = UserSerializer(user)

        return Response({
            "user": serializer.data,
            "enterprise": enterprise,
            "refresh": str(token),
            "access_token" : token.access_token
        })

