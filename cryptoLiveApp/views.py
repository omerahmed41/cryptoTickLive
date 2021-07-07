from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import views as authtoken_views
from .ExchangeRateHelper import ExchangeRateHelper
from rest_framework.decorators import authentication_classes, permission_classes
from django.http import HttpResponse, HttpRequest


MainProject = """
<!DOCTYPE html>
<html>
<head>
<title> Live bitcoin price </title>
<style>
    body {
        width: 1000px;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
  
</style>
</head>
<body>
  <div>
   <h2>Live bitcoin price updated every hourt</h2>
<ul>
  <li>We fetches the price of BTC/USD from the alphavantage API.</li>
  <li> WE fetches every hour.</li>
  <li> 3.Then stores it on postgres.</li>
  <li>  4.We have 2 secure APIs that you need an API key to use it. we have a two endpoints:
<ul>
  <li> i. GET /api/v1/quotes - returns exchange rate.</li>
  <li> ii. POST /api/v1/quotes which triggers force requesting of the price from alphavantage.</li>
</ul>  
    </li>

  <li>5. The API & DB is containerized using Docker.</li>
  <li>6. All sensitive data such as alphavantage API key, are passed from the .env "gitignored" file via environment variables.</li>
</ul>  

<a href="https://github.com/omerahmed41/cryptoTickLive">Find the Code on GitLab</a>
  </div>
</body>
</html>
"""

@authentication_classes([])
@permission_classes([])
class index(APIView):
    def get(self, request):
       return HttpResponse(MainProject.replace("{IPADDRESS}",request.get_host()))
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


