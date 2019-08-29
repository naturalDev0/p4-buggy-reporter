from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages

# Create your views here.
def login():
    pass

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('Index'))