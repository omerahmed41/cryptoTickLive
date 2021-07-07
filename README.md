# cryptoTickLive
Python Django- Show the price of Bitcoin live

cryptoLive
Live bitcoin price updated every hour

We fetches the price of BTC/USD from the alphavantage API.
WE fetches every hour. 3.Then stores it on postgres. 4.We have 2 secure APIs that you need an API key to use it.
we have a two endpoints: i. GET /api/v1/quotes - returns exchange rate and ii. POST /api/v1/quotes which triggers force requesting of the price from alphavantage.
The API & DB is containerized using Docker.
All sensitive data such as alphavantage API key, are passed from the .env "gitignored" file via environment variables.


1. We are using oauth 2.0 to access the api pass 'Authorization:Token userToken' in the header
example curl http://www.cryptotick.live/api/v1/quotes/ -H 'Authorization: Token 6dd9a0f5d9915eee0ff5dc0e99927f3d76467cc3'

2. To get access Token use Post http://www.cryptotick.live/token-auth/ 
username:omer
password:12341234


3. To get the last price on our Database use:
Get http://www.cryptotick.live/api/v1/quotes/

To force requesting of the price from alphavantage. use
POST http://www.cryptotick.live/api/v1/quotes/
