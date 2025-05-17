from accounts.views.base import BaseView
from accounts.models import User
from accounts.serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GetUser(BaseView):
    permission_classes = [IsAuthenticated]

    def get(self,request) -> None:
        # Implement the logic to get the user details here
        user = User.objects.get(id=self.request.user.id).first()
        enterprise = self.get_enterprise_user(user.id)

        serializer = UserSerializer(user)

        return Response({
            "user": serializer.data,
            "enterprise": enterprise
        })