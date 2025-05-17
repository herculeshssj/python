from accounts.views.signin import SignIn
from accounts.views.signup import Signup
from django.urls import path


urlpatterns = [
    path('signin', SignIn.as_view()),
    path('signup', Signup.as_view()),
]