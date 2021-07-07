
from background_task import background
from django.conf import settings as conf_settings
import requests
from .models import ExchangeRate
import json
from django.core import serializers
from django.http import HttpResponse


class ExchangeRateHelper():
    def getLastExchangeRateFromDB(self):
        q = ExchangeRate.objects.last()
        serialized_obj = serializers.serialize("json",[q])
        return HttpResponse(serialized_obj, content_type='application/json')

    @background(queue='cryptoLiveQueue')
    def schedule(self):
     getExchangeRate('BTC','USD')

    def getExchangeRate(self, fromCurrency,toCurrency):
            apikey = conf_settings.ALPHAVANTAGE_KEY    
            url = ("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency="+
            fromCurrency+"&to_currency="+toCurrency+"&apikey="+apikey)

            result =  self.makeHttpGETRequest(url) 
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

    def makeHttpGETRequest(self,url):
        try:
                r = requests.get(url)
                response = r.json()
                if r.status_code == 200:
                    return self.responseObj(True,r.status_code,response)
                else:
                    return self.responseObj(False,r.status_code)
        except  requests.RequestException as e:
                return self.responseObj()


    def responseObj(self, state = False ,code = None ,response = None):
        return {
                    "state": state ,
                    "status_code" : code,
                    "response": response
            }