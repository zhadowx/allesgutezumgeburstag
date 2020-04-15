from transactions import *
from promotion import *

items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
running = True

while running:
	option = 1
	for choice in items:
		print(str(option) + ". " + choice)
		option = option + 1
	print(str(option) + ". Quit")
	choice = int(input("Choose an option: "))
	if choice == option:
		running = False
	else:
		credit_card = input("Credit card number: ")
		new_price=discount(prices[choice-1])
		save_transaction(new_price, credit_card, items[choice-1])