from django.shortcuts import render, reverse, HttpResponse
from django.conf import settings

# Create your views here.
import stripe

def donate(request):
    return render(request, 'payment_donate.html')
    
def charge(request):
    amount = int( request.GET['amount']) * 100
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(payment_method_types=['card'],
        line_items=[
            {
                'name': 'Donation',
                'description':'A simple donation',
                'amount':amount ,
                'currency':'usd',
                'quantity':1
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
    return HttpResponse("<h1>We have gotten your money</h1>")
    
def cancel(request):
    return HttpResponse("<h1>No, don't go!</h1>")