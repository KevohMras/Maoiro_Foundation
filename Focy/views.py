from django.shortcuts import redirect

from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View

import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from Focy.credentials import MpesaAccessToken, MpesaC2bCredential, LipanaMpesaPpassword


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')


def service(request):
    return render(request, 'service.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def token(request):
    consumer_key = 'nnuypckGY97scmh2TZPqrgtBit5d17KU'
    consumer_secret = 'HtbS2lE3mrMieXiM'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})


# returning stk push
def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Acer Enterprises",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Message sent successful")


def pay(request):
    return render(request, 'pay.html')

# listings/views.py
def contact(request):
  form = contact()# instantiate a new form here
  return render(request, 'contact.html', {'form': form}) # pass that form to the template