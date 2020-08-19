from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse
import json

from django.views.generic import View
from .mixin import HttpResponseMixin

class Message(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        message = "Hello! Ashish"
        return HttpResponse(message)
    
