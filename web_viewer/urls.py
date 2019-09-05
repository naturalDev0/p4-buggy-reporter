from django.urls import path, include
from .views import create_bugs, edit_bugs

urlpatterns = [
    path('create/', create_bugs, name='create_bugs'),
    path('edit/<id>', edit_bugs, name='edit_bugs')
]