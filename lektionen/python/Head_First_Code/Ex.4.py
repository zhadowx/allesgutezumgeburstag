from random import randint

def is_integer(str):
	num_dict={"0","1","2","3","4","5","6","7","8","9"}
	for s in str:
		if s not in num_dict:
			return False
	return True


secret = randint(1,50)
print ("Welcome!")
messages=["Try numerical value (T_T)",
		  "Plz numerical value...",
		  "I said numerical value #@!$",
		  "Mothafucka you dumb?",
		  "Numbers Numbers",
		  "No more warnings (notice this is a warning though)",
		  "Fuck it! You lose now (x_x)"
		  ]
# print("len(messages): "+str(len(messages))) #testing
i=0
#guess=0 #also a valid assignment
guess = secret+1
while guess != secret:
	g = input("Guess the number: ")
	if not is_integer(g):
	# if is_integer(g)== False:
	# if is_integer(g)!= True:
		print(messages[i])
		i=i+1
		# print("i: "+str(i)) #testing
		if (i==len(messages)):
			break #get out of loop 
		continue #restart loop

	if guess == secret:
		print("You win!")
	else:
		if guess < secret:
			print("Too low!")
		else:
			print("Too high!")
print("Game over!")