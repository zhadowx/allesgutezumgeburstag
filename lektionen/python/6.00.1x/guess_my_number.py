low = 0
high = 100
secret = (low + high) // 2

print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(secret) + "?")
inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while inp != "c":
  if inp == "l":
    low = secret
    secret = (low + high) // 2
    print("Is your secret number " + str(secret) + "?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ") 
  
  elif inp == "h":
    high = secret
    secret = (low + high) // 2
    print("Is your secret number " + str(secret) + "?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  
  else:
    print("Sorry, I did not understand your input.")  
    print("Is your secret number " + str(secret) + "?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was: " + str(secret))