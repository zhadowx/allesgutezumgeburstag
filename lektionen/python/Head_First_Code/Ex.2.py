print ("Welcome")
g= input("Guess the number: ")
guess= int(g)
if guess == 5:
	print("You Win!")
else:
	if guess < 5:
		print("Too low!")
	else:
	 	print("Too high!")
print("Game over!")