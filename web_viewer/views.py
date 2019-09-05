from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Bug
from .forms import BugReportForm

# Home page
def index(request):
    results = Bug.objects.all()
    return render(request, 'index.html', {
        'bugs' : results
    })
    
# Report bugs
def create_bugs(request):
    
    if request.method == 'POST':
        # Process the form
        form = BugReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        pass
    else:
        form = BugReportForm()
        return render(request, "create_bugs.html", {
            'form' : form
        })
        
def edit_bugs(request, id):
    
    bug = get_object_or_404(Bug, pk=id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        pass
    
    else:
        form = BugReportForm(instance=bug)
        return render(request, 'create_bugs.html', {
            'form' : form
        })
    
    