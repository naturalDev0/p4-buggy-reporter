from django.urls import path, include
from .views import login, logout, profile, register

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name='logout'),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile")
]