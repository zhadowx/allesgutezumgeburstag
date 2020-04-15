import urllib.request
page=urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
text=page.read().decode("utf8")
where=text.find(">$")
start=where+2
end=where+6
price=text[start:end]
print(price)
