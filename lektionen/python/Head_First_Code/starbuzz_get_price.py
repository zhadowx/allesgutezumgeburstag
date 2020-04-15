import urllib.request
import time

password = "gfdsahjkl07"

def get_price():
	page = urllib.request.urlopen("file:///D:/Study/Computer Science/Python/prices-royalty.html")
	text = page.read().decode("utf8")
	where_in_text = text.find(">$")
	price = float(text[where_in_text+2:where_in_text+6])
	return(price)
	# return (price)
def send_to_twitter(sage):
	msg = sage + "!" + " The price is: " + str(get_price())
	password_manager = urllib.request.HTTPPasswordMgr()
	password_manager.add_password("Twitter API", "http://twitter.com/statuses", "trolero08469902", password)
	http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
	page_opener = urllib.request.build_opener(http_handler)
	urllib.request.install_opener(page_opener)
	params = urllib.parse.urlencode( {'status': msg} )
	resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
	resp.read()

qst = input("Is the price required inmediately (Y/N): ")
ask = str(qst)
if ask == "Y":
	price = 99.99
	get_price()
	send_to_twitter("Emergency")
else:
	price = 99.99
	while price > 4.74:
		time.sleep(900)
		get_price()
		send_to_twitter("Low price")
		