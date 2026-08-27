from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from demo.models import Funds,Investment
from demo.serializers import FundsSerializer,InvestSerializer
from datetime import datetime


class FundsList(generics.ListCreateAPIView):
    queryset = Funds.objects.all()
    serializer_class = FundsSerializer

class FundsChange(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Funds.objects.all()
    serializer_class = FundsSerializer
    lookup_url_kwarg = 'fund_id'


class InvestList(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestSerializer

@csrf_exempt
@api_view(['POST'])
def calculateCurrentValue(request):
    data = request.data
    scheme_code = data['scheme_code']
    date = datetime.today().date()
    units = 0
    current_value = 0
    fund_obj = Funds.objects.filter(scheme_code=scheme_code,date=date)
    if fund_obj.exists():
        investObj = Investment.objects.filter(fundId_id=data['fund_id'])
        if investObj.exists():
            units = investObj[0].units_purchased
            current_value = units * fund_obj[0].net_asset_value

    if current_value:
        return HttpResponse(current_value)
    else:
        return HttpResponse(0)
    