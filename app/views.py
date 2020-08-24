from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse
import json

from django.views.generic import View
from .mixin import HttpResponseMixin

from twilio.twiml.messaging_response import MessagingResponse

# from twilio.rest import Client
import os

# account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
# auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
#
# def send(msg):
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#           from_='whatsapp:+14155238886',
#           body=msg,
#           to='whatsapp:+919911698098'
#                               )
#     print("send!")

def home(request):
    return HttpResponse("Hello World!")

from django.views.decorators.csrf import csrf_exempt



# class Message(View):
#     def post(self,request,*args,**kwargs):
#         # message = "Hello! Ashish"
#         # send(request.POST.get('Body'))
#         print("jj")
#         msg = request.values.get('Body', '').lower()
#         resp = MessagingResponse()
#         res.message()
#         print(msg)
#         return str(resp)

@csrf_exempt
def message(request):
    # if request.method == "POST":
        print("jj")
        ms = request.POST.get('Body', '').lower()
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(ms)
        # msg.media('https://thumbs.gfycat.com/EqualTotalBlackfly-size_restricted.gif')
        print(ms)
        return HttpResponse(str(resp))
