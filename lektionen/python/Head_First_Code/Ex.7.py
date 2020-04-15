import urllib.request
import time

def get_price():
	page=urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
	text=page.read().decode("utf8")
	where=text.find(">$")
	start=where+2
	end=where+6
	price=float(text[start:end])
	return(price)
	

print ("Welcome!")
price_now=input("Is the price requiered inmediately (Y/N)? ")
if price_now == "Y":
	price=get_price()
	print(price)
else:
	price=99
	while price > 4.74:
		time.sleep(900)
		price=get_price()
	print("Buy!")