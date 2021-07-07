from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import views as authtoken_views
from django.http import HttpResponse
import requests
from .models import ExchangeRate
import json
from django.http import HttpResponse
from background_task import background
from django.core import serializers
from django.conf import settings as conf_settings


class index(APIView):
    def get(self, request):
       content = {'message': 'Live bitcoin price updated every hour'}
       return Response(content)
       return getLastExchangeRateFromDB()


class QuotesView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
       return getLastExchangeRateFromDB()

    def post(self, request):
        schedule( repeat=30,repeat_until= None)
        if (getExchangeRate('BTC','USD') == True):
              return getLastExchangeRateFromDB()
        else:
              return  Response('Unable to get the exchangeRate')


def getLastExchangeRateFromDB():
     q = ExchangeRate.objects.last()
     serialized_obj = serializers.serialize("json",[q])
     return HttpResponse(serialized_obj, content_type='application/json')

@background(queue='cryptoLiveQueue')
def schedule():
   getExchangeRate('BTC','USD')

def getExchangeRate(fromCurrency,toCurrency):
        apikey = conf_settings.ALPHAVANTAGE_KEY    
        url = ("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency="+
        fromCurrency+"&to_currency="+toCurrency+"&apikey="+apikey)

        result =  makeHttpGETRequest(url)
#         return result
        if result["state"] == True :
            response =  result["response"]
            if "Realtime Currency Exchange Rate" in response.keys():
                realtimeCurrencyExchangeRate = response[ "Realtime Currency Exchange Rate"]
                exchangeRate =  realtimeCurrencyExchangeRate["5. Exchange Rate"]
                b = ExchangeRate(exchangeRate=exchangeRate)
                b.save()
                return  True
            else:
                return False

        else:
            return  False

def makeHttpGETRequest(url):
       try:
              r = requests.get(url)
              response = r.json()
              if r.status_code == 200:
                  return responseObj(True,r.status_code,response)
              else:
                  return responseObj(False,r.status_code)
       except  requests.RequestException as e:
             return responseObj()


def responseObj(state = False ,code = None ,response = None):
    return {
                 "state": state ,
                 "status_code" : code,
                 "response": response
           }