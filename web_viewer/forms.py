from django import forms
from .models import Bug

class BugReportForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'done', 'completed_at', 'category', 'tags')