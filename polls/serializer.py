# yourapp/serializers.py

from rest_framework import serializers
from .models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'  # Or specify specific fields like ['id', 'field1', 'field2']
