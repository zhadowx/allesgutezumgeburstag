print ("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess > 5:
	print("Too high!")
else:
	if guess < 5:
		print("Too low!")
while guess != 5:
	g = input("Guess the number: ")
	guess = int(g)
	if guess > 5:
		print("Too high!")
	else:
		if guess < 5:
			print("Too low!")
print("You win!")
print("Game over!")	