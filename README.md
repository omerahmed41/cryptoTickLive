# cryptoTickLive
Python Django- Show the price of Bitcoin live

cryptoLive
Live bitcoin price updated every hour

We fetches the price of BTC/USD from the alphavantage API.
WE fetches every hour. 3.Then stores it on postgres. 4.We have 2 secure APIs that you need an API key to use it.
we have a two endpoints: i. GET /api/v1/quotes - returns exchange rate and ii. POST /api/v1/quotes which triggers force requesting of the price from alphavantage.
The API & DB is containerized using Docker.
All sensitive data such as alphavantage API key, are passed from the .env "gitignored" file via environment variables.
