from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Account - Login
def login(request):
    
    # Returns the login page
    if request.method == 'POST':
        
        # Populate the form from what the user has keyed in
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            
            # Attempt to check the username and password is valid
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            messages.success(request, "You have successfully logged in")
            
            if user:
                # log in the user
                auth.login(user=user, request=request)
                return redirect(reverse('Index'))
            else:
                login_form.add_error('None', "Invalid username or password")
                
    else:
        login_form = UserLoginForm
        return render(request, 'account_login.html', {
            'form':login_form
        })

# Account - Logout    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('Index'))

@login_required
def profile(request):
    return HttpResponse("Profile")
    
# Register User
def register(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
            
            return redirect(reverse('Index'))
            
        else:
            return render(request, "account_register.html", {
                'form' : form
            })
    else:
        form = UserRegistrationForm()
        return render(request, 'account_register.html', {
            'form' : form
        })
    