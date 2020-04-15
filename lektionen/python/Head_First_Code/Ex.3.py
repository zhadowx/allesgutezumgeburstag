from random import randint
secret = randint(1,1+000)
print ("Welcome!")
messages=["Try numerical value (T_T)",
		  "Plz numerical value...",
		  "I said numerical value #@!$",
		  "Mothafucka you dumb?",
		  "Numbers Numbers",
		  "Fuck it! You lose now x_x",
		  ]
# print("len(messages): "+str(len(messages))) #testing
i=0
#guess=0 #also a valid assignment
guess = secret+1
while guess != secret:
	g = input("Guess the number: ")
	
	#exception handling
	try:
		guess=int(g)			
	except:
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