from django.urls import path
from .views import BankTransferView, BankTransactionListView

urlpatterns = [
    path('bank-transfer/', BankTransferView.as_view(), name='bank-transfer'),
    path('bank-transactions/', BankTransactionListView.as_view(), name='bank-transactions'),
]
