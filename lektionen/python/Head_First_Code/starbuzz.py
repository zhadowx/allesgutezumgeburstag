import urllib.request
import time
price = 99.99
while price > 4.74:
	time.sleep(900)
	page = urllib.request.urlopen("file:///D:/Study/Computer Science/Python/prices-royalty.html")
	text = page.read().decode("utf8")
	where_in_text = text.find(">$")
	price = float(text[where_in_text+2:where_in_text+6])
print("Buy!")