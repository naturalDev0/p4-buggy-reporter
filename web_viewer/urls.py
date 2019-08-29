from django.urls import path, include
from .views import show_bug_viewer, create_bugs, edit_bugs

urlpatterns = [
    path('bugs/', show_bug_viewer),
    path('bugs/new/', create_bugs),
    path('bugs/edit/<id>', edit_bugs)
]