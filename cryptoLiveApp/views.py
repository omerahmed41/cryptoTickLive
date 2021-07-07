from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import views as authtoken_views
from .ExchangeRateHelper import ExchangeRateHelper
from rest_framework.decorators import authentication_classes, permission_classes


@authentication_classes([])
@permission_classes([])
class index(APIView):
    def get(self, request):
       content = {'message': 'Live bitcoin price updated every hour'}
       return Response(content)
       #return ExchangeRateHelper.getLastExchangeRateFromDB()


class QuotesView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
       er =  ExchangeRateHelper()
       return er.getLastExchangeRateFromDB()

    def post(self, request):
        er =  ExchangeRateHelper()
        #er.schedule( repeat=30,repeat_until= None)

        if (er.getExchangeRate('BTC','USD') == True):
                er =  ExchangeRateHelper()
                return er.getLastExchangeRateFromDB()
        else:
              return  Response('Unable to get the exchangeRate')


