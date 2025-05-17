from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from companies.models import Enterprise, Employee

from accounts.models import UserGroup, GroupPermission

class BaseView(APIView):
    def get_enterprise_user(self, user_id) -> dict[str, any] | None:
        enterprise = {
            "is_owner": False,
            "permissions": []
        }

        enterprise['is_owner'] = Enterprise.objects.filter(
            user_id=user_id
        ).exists()

        if enterprise['is_owner']:
            return enterprise
        
        # Permissions , Get Employee
        employee = Employee.objects.filter(
            user_id=user_id
        ).first()

        if not employee:
            raise APIException("User not found")
        
        # Get Permissions
        groups = UserGroup.objects.filter(
            user_id=user_id
        ).all()

        for group in groups:
            group = g.group

            permissions = GroupPermission.objects.filter(
                group_id=group.id
            ).all()

            for p in permissions:
                enterprise['permissions'].append({
                    "id":p.permission.name,
                    "label":p.permission.name,
                    "codename":p.permission.codename
                }) 

        return enterprise