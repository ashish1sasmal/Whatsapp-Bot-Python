from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse
import json

from django.views.generic import View
from .mixin import HttpResponseMixin

from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

def send(msg):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
          from_='whatsapp:+14155238886',
          body=msg,
          to='whatsapp:+919911698098'
                              )
    print("send!")

class Message(HttpResponseMixin,View):
    def post(self,request,*args,**kwargs):
        message = "Hello! Ashish"
        send(request.POST('Body'))
        return HttpResponse(message)
