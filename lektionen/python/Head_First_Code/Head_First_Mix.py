from tkinter import *
import pygame.mixer

mixer = pygame.mixer
mixer.init()

sound_file = "50459_M_RED_Nephlimizer.wav"

track = mixer.Sound(sound_file)

# def track_start():
#   track.play(loops = -1)

# def track_stop():
#   track.stop()

def shutdown():
  mixer.stop()
  app.destroy()

def track_toggle():
  if track_playing.get() == 1:
    track.play(loops = -1)
  else:
    track.stop()

def change_volume(v):
  track.set_volume(volume.get())

app = Tk()
app.title("Head First Mix")

volume = DoubleVar()
volume.set(track.get_volume())
volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0, resolution = 0.01, command = change_volume, label = "Volume", orient = HORIZONTAL)
volume_scale.pack(side = RIGHT)

track_playing = IntVar()

track_button = Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file)
track_button.pack()
# start_button = Button(app, command = track_start, text = "Start")
# start_button.pack(side = LEFT)

# stop_button = Button(app, command = track_stop, text = "Stop")
# stop_button.pack(side = RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
