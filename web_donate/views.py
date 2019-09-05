from django.shortcuts import render, reverse, HttpResponse, redirect
from django.contrib import messages
from django.conf import settings

# Create your views here.
import stripe

def donate(request):
    return render(request, 'payment_donate.html')
    
def charge(request):
    get_amount = request.GET['amount']
    if get_amount == '':
        # messages.error(request, 'Please insert a value.')
        return redirect(reverse('donate'))
    else:
        amount = int(get_amount) * 100
        if amount == 0:
            # messages.error(request, 'Please insert a value more than 0.')
            # return redirect(reverse('donate'), error_message='Please insert a value more than 0.')
            return redirect(reverse('donate'))
        
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(payment_method_types=['card'],
        line_items=[
            {
                'name' : 'Donation',
                'description' : 'A simple donation to support BuggyReporter',
                'amount' : amount ,
                'currency' : 'sgd',
                'quantity' : 1
            }
        ],
        success_url= request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel'))
    )
    return render(request, 'payment_charge_donate.html', {
        'CHECKOUT_SESSION_ID': session.id,
        'publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })

    
def success(request):
    messages.success(request, "You have successfully made a donation.")
    return redirect(reverse('index'))
    # return HttpResponse("<h1>We have gotten your money</h1>")
    
def cancel(request):
    messages.error(request, "You have cancelled a donation.")
    return redirect(reverse('donate'))
    
    # return HttpResponse("<h1>No, don't go!</h1>")