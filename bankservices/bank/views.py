from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BankTransfer
from .serializers import BankTransferSerializer


class BankTransferView(APIView):
    def post(self, request):
        serializer = BankTransferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BankTransactionListView(APIView):
    def get(self, request):
        bank_transfers = BankTransfer.objects.all()
        serializer = BankTransferSerializer(bank_transfers, many=True)
        return Response(serializer.data)
