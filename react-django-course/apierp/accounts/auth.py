from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import make_password, check_password

from accounts.models import User
from companies.models import Enterprise, Employee

class Authentication:
    def signin(self, email=None, password=None) -> User:
        exception_auth = AuthenticationFailed('Email e/ou senha inválidos')
        
        user_exists = User.objects.filter(email=email).exists()
        
        if not user_exists:
            raise exception_auth
        
        user = User.objects.get(email=email).first()

        if not check_password(password, user.password):
            raise exception_auth
        
        return user
    
    def signup(self, name=None, email=None, password=None, type_account='owner', company_id=False) -> User:
        if not name or name == '':
            raise APIException('O nome não deve ser vazio')
        if not email or email == '':
            raise APIException('O email não deve ser vazio')
        if not password or password == '':
            raise APIException('A senha não deve ser vazia')
        if not type_account == 'employee' and not company_id:
            raise APIException('O id da empresa não foi informado')
        
        user = User
        if User.objects.filter(email=email).exists():
            raise APIException('Email já cadastrado')
        
        password_hashed = make_password(password)
        created_user = User(
            name=name,
            email=email,
            password=password_hashed,
            is_owner = 0 if type_account == 'employee' else 1
        )

        if type_account == 'owner':
            created_enterprise = Enterprise.objects.create(
                name='Nome da empresa',
                owner=created_user
            )

        if type_account == 'employee':
            Employee.objects.create(
                enterprise_id = company_id or created_enterprise.id,
                user=created_user.id
            )

        return created_user