from django.shortcuts import render, HttpResponse, redirect
from .models import Bug
from .forms import BugReportForm

# Home page
def index(request):
    return render(request, 'index.html')

# Show reported bugs
def show_bug_viewer(request):
    
    # THIS IS FOR TESTING DJANGO ONLY
    # return HttpResponse("Hello World")
    results = Bug.objects.all()
    return render(request, "show_bugs.html", {
        'bugs' : results
    })
    
# Report bugs
def create_bugs(request):
    
    if request.method == 'POST':
        # Process the form
        form = BugReportForm(request.POST, request.FILES)
        print('something wrong')
        if form.is_valid():
            form.save()
            return redirect(show_bug_viewer)
    else:
        form = BugReportForm()
        print('something wrong')
        return render(request, "create_bugs.html", {
            'form' : form
        })
    
    
    