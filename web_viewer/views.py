from django.shortcuts import render, HttpResponse
from .models import Bug

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
    return render(request, "create_bug.html")
    
    
    