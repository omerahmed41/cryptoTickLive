
from background_task import background
from django.conf import settings as conf_settings
from .models import ExchangeRate
import json
from django.core import serializers
from django.http import HttpResponse
from .HttpRequestHelper import HttpRequestHelper

class ExchangeRateHelper():

    @background(queue='cryptoLiveQueue')
    def schedule():
      er =  ExchangeRateHelper()      
      er.getExchangeRate('BTC','USD')


    def getLastExchangeRateFromDB(self):
        q = ExchangeRate.objects.last()
        serialized_obj = serializers.serialize("json",[q])
        return HttpResponse(serialized_obj, content_type='application/json')



    def getExchangeRate(self, fromCurrency,toCurrency):
            apikey = conf_settings.ALPHAVANTAGE_KEY    
            url = ("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency="+
            fromCurrency+"&to_currency="+toCurrency+"&apikey="+apikey)

            httpHelper = HttpRequestHelper()
            result =  httpHelper.makeHttpGETRequest(url) 
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

   