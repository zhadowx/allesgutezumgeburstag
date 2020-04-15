#Import the libraries that you need!
from tkinter import *
import pygame.mixer

#Initialize the sound system
sounds = pygame.mixer
sounds.init()

#Load in the requires sound effects
sound_correct = sounds.Sound("correct.wav")
sound_wrong = sounds.Sound("wrong.wav")

#Create the two event handlers that set IntVar and Sounds
def correct_answers():
  num_good.set(num_good.get() + 1)
  sound_correct.play()

def wrong_answers():
  num_bad.set(num_bad.get() + 1)
  sound_wrong.play()

#Create GUI app window
app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

#Create two IntVars: to count correct and wrong ans.
num_good = IntVar()
num_good.set(0)

num_bad = IntVar()
num_bad.set(0)

#Display friendly message to tell the user :D
l0 = Label(app, text = 'When you are ready click on the buttons!', height = 3)
l0.pack()

#Create two labels to hold each counter and connect them with IntVars.
l1 = Label(app, textvariable = num_good)
l1.pack(side = 'left')

l2 = Label(app, textvariable = num_bad)
l2.pack(side = 'right')

#Create each of the buttons and connect them to their event handler
b1 = Button(app, text = "Correct!", width = 10, command = correct_answers)
b2 = Button(app, text = "Wrong!", width = 10, command = wrong_answers)

b1.pack(side = 'left', padx = 10, pady = 10)
b2.pack(side = 'right', padx = 10, pady = 10)

#Start tkinter's main event loop
app.mainloop()


