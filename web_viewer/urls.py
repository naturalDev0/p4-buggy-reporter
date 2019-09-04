from django.urls import path, include
from .views import show_bug_viewer, create_bugs, edit_bugs

urlpatterns = [
    path('', show_bug_viewer),
    path('new/', create_bugs),
    path('edit/<id>', edit_bugs)
]