from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='username'),
    # path('Users/',views.Users,name='test'),
    # path('signUp/',views.signUp,name='signUp'),
]