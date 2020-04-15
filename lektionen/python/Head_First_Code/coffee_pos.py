from transactions import *
import promotion 
import starbuzzi 

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.0, 1.80, 1.20]
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
		discount_card = input("Starbuzz Discount Card?: Y/N ")
		if discount_card == "Y":
			card_price = starbuzzi.discount(prices[choice-1])
			new_price = promotion.discount(card_price)
			save_transaction(new_price, credit_card, items[choice-1])
		else:
			new_price = promotion.discount(prices[choice-1])
			save_transaction(new_price, credit_card, items[choice-1])