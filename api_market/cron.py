def gather_price():

	import requests
	from api_market.models import Prices

	url='https://api.bittrex.com/v3/markets/BTC-USDT/summary'
	resp=requests.get(url)
	data=resp.json()
	updatedAt, high, low = data['updatedAt'], data['high'], data['low']
	#print(f'updatedAt: {updatedAt}')

	p=Prices.objects.create(high=high, low=low, updatedAt=updatedAt)