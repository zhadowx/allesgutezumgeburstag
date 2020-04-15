from random import randint
secret = randint (1,10)
print ("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess > secret:
	print ("Too high!")
else:
	if guess < secret:
		print("Too low!")
while guess != secret:
	print("Try again!")
	g = input("Guess the number: ")
	guess = int(g)
	if guess > secret:
		print ("Too high!")
	else:
		if guess < secret:
			print("Too low!")
print("You win!")
print("Game over!")