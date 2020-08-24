from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import View
from .mixin import HttpResponseMixin
from twilio.twiml.messaging_response import MessagingResponse
import requests

def home(request):
    return HttpResponse("Hello World!")

from django.views.decorators.csrf import csrf_exempt
import requests

def weather(lat,long):
    url=f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=92c0450a31e8cb64bf9247d0370fcec2"
    r = requests.get(url = url)
    data = r.json()['main']
    s=f"""
        CURR TEMP: {round(data['temp']-273.15,2)} °C,\n
        FEELS LIKE: {round(data['feels_like']-273.15,2)} °C,\n
        MIN TEMP: {round(data['temp_min']-273.15,2)} °C,\n
        MAX TEMP: {round(data['temp_max']-273.15,2)} °C, \n
        PRESSURE: {data['pressure']}, \n
        HUMIDITY: {data['humidity']}
    """
    return(s)

@csrf_exempt
def message(request):
    # if request.method == "POST":
        print("jj")
        ms = weather(28.7041,77.1025)
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(ms)
        # msg.media('https://thumbs.gfycat.com/EqualTotalBlackfly-size_restricted.gif')
        print(ms)
        return HttpResponse(str(resp))

#
