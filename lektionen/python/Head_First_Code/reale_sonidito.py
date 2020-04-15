from Trial_sounds import *

number_asked = 0 
number_correct = 0
number_wrong = 0

# ask the host to press 1 for correct, 2 for incorrect, or 0 
# to end while the host response is not 0

while True:
  host_response = int(input("Press 1 for corect or 2 for incorrect or 0 to end"))
  if host_response ==  1:
    number_asked = number_asked + 1
    number_correct =  number_correct + 1
    sound_correct = sounds.Sound("correct.wav")
    wait_finish(sound_correct.play())
  elif host_response == 2:
    number_asked = number_asked + 1
    number_wrong =  number_wrong + 1
    sound_wrong = sounds.Sound("wrong.wav")
    wait_finish(sound_wrong.play())
  else:
    break

# Display the values of number_asked, number_correct and 
# number_wrong on screen

print("You asked " + str(number_asked) + " questions" + "\n" + str(number_correct) + " were correctly answered"  
  + "\n" + str(number_wrong) + " were answered incorrectly")

