from django.http import JsonResponse
from django.shortcuts import render
import json

# Create your views here.

def apiHome(req,*args,**kwargs):
    return JsonResponse({"message":"Hi there this is your django api"})


def postApi(req,*args,**kwargs):
    body = req.body
    data = {}
    try:
        data = json.loads(body)
        data['returnMessage'] = 'Sure lets do it'
    except:
        pass
    return JsonResponse(data)