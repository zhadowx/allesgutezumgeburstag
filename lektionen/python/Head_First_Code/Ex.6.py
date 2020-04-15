import urllib.request
import time

price=99
while price >4.74:
	time.sleep(900)
	page=urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
	text=page.read().decode("utf8")
	where=text.find(">$")
	start=where+2
	end=where+6
	price=float(text[start:end])

print("Buy!")
