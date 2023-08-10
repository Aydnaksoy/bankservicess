from rest_framework import serializers
from .models import BankTransfer


class BankTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransfer
        fields = '__all__'
