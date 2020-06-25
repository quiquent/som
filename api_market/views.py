from django.shortcuts import render

def grafica(request):

	import io,urllib, base64
	import matplotlib.pyplot as plt
	from api_market.models import Prices
	
	highs=[]
	lows=[]
	dates=[]
	p=Prices.objects.all()
	prices=p.values()

	for price in prices:
		highs.append(float(price["high"]))
		lows.append(float(price["low"]))
		dates.append(price["updatedAt"])

	plt.plot(range(len(dates)), lows)
	plt.plot(range(len(dates)), highs)
	fig=plt.gcf()
	buf=io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string=base64.b64encode(buf.read())
	uri=urllib.parse.quote(string)

	#context = {'prices': prices}
	context={'data':uri}
	return render(request, 'api_market/grafica.html', context)
