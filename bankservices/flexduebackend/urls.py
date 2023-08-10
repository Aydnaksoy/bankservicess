from django.urls import path
from .views import UserView, LoanRequestView, BankTransferView

urlpatterns = [
    path('user/', UserView.as_view(), name='user'),
    path('loan-request/', LoanRequestView.as_view(), name='loan-request'),
    path('bank-transfer/', BankTransferView.as_view(), name='bank-transfer'),
]
