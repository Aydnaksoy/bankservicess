from rest_framework import serializers
from user.models import User
from loan.models import LoanRequest
from bank.models import BankTransfer


# User Services Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# Loan Services Serializers
class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'


# Bank Services Serializers
class BankTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransfer
        fields = '__all__'
