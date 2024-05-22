import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import  Transactions
from .serializer import TransactionSerializer
from django.shortcuts import get_object_or_404

# Create your views here.



def apiHome(req,*args,**kwargs):
    param = req.GET.get('id')
    transactionData = get_object_or_404(Transactions,pk=param)
    ser = TransactionSerializer(transactionData)
    data = ser.data
    return JsonResponse({"data" : data})