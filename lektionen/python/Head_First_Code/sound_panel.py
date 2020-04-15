from tkinter import *
import pygame.mixer

def create_gui(app, mixer, sound_file):
  def track_toggle():
    if track_playing.get() == 1:
      track.play(loops = -1)
    else:
      track.stop()

  def change_volume(v):
    track.set_volume(volume.get())

  track = mixer.Sound(sound_file)
  track_playing = IntVar()
  track_button = Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file)
  track_button.pack()
  volume = DoubleVar()
  volume.set(track.get_volume())
  volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0, resolution = 0.01, command = change_volume, label = "Volume", orient = HORIZONTAL)
  volume_scale.pack()
  