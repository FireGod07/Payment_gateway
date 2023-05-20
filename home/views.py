from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
import razorpay
from gateway.settings import razor_pay_key_id,razor_pay_key_secret
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request,"index.html")
    
def payment(request):
    client = razorpay.Client(auth=(razor_pay_key_id, razor_pay_key_secret))
    if request.method == 'POST':
        amount = int(request.POST.get('amount'))*100
        name = request.POST.get('name')
        email = str(request.POST.get('email'))
        DATA = {
            "amount": amount,
            "currency": "INR",
            "receipt": "receipt#1",
            "notes": {
                "key1": "value3",
                "key2": "value2"
            },
            "payment_capture":1
        }
        payment_order = client.order.create(data=DATA)
        context = {
            'api_key' : razor_pay_key_id,
            'payment_order_id' : payment_order['id'],
            'amountPaise' : amount,
            'amountInr' : amount/100,
            'name' : name,
            'email' : email
        }

        # send_mail(
        #     'Thanks for donation',
        #     f"""
        #     Dear {name},
        #     We are truly inspired by your kindness and compassion. It is because of donors like you that we are able to [describe the work or projects undertaken]. Your belief in our cause motivates us to continue striving towards our goals and making a positive difference in the world.Once again, thank you from the bottom of our hearts for your generosity. Your support is invaluable and greatly appreciated. We would not be able to accomplish what we do without supporters like you.

        #     Donation Info:
        #     Amount : {amount/100}
        #     """
        #     ,
        #     'damnation742@gmail.com',
        #     [email,],
        #     fail_silently = False,
        # )
        return render(request,"payment.html",context)


