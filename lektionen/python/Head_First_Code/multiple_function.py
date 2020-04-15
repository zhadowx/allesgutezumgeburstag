from tkinter import *
import pygame.mixer

mixer = pygame.mixer
mixer.init()

music = ["59264_M_RED_TheDreamDrums.wav", "50848_M_RED_WaveBaseLoop.wav", "50459_M_RED_Nephlimizer.wav", "49119_M_RED_HardBouncer.wav", "45414_M_RED_Trance_Train.wav", "41722__M_RED__happy_freaq.wav", "41312_M_RED_Sonar_Line.wav", "39607__M_RED__trumpet_delay_loop.wav", "39484__M_RED__trance_trumpet_loop.wav", "39147_M_RED_beep_line.wav"]
widget_dict = {}
  # track = mixer.Sound(sound_file)


def shutdown():
  widget_dict['track'].stop()
  app.destroy()

def track_toggle():
  if widget_dict['track_playing'].get() == 1:
    widget_dict['track'].play(loops = -1)
  else:
    widget_dict['track'].stop()

def change_volume(v):
  widget_dict['track'].set_volume(widget_dict['volume'].get())

app = Tk()
app.title("Head First Mix")

def create_widgets(sound_file):
  
  # volume = DoubleVar()
  widget_dict['volume'] = DoubleVar()
  widget_dict['volume'].set(widget_dict['track'].get_volume())
  widget_dict['scale'] = Scale(app, variable = widget_dict['volume'], from_ = 0.0, to = 1.0, resolution = 0.01, command = change_volume, label = "Volume", orient = HORIZONTAL)

  # volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0, resolution = 0.01, command = change_volume, label = "Volume", orient = HORIZONTAL)
  # volume_scale.pack(side = RIGHT)
  widget_dict['scale'].pack(side = RIGHT)
  widget_dict['track_playing'] = IntVar()
  # track_playing = IntVar()
  widget_dict['track_button'] = Checkbutton(app, variable = widget_dict['track_playing'], command = track_toggle, text = sound_file)
  widget_dict['track_button'].pack()
  
  return widget_dict
  # track_button = Checkbutton(app, variable = widget_dict['track_playing'], command = track_toggle, text = sound_file)
  # track_button.pack()

# w_list=[]
# for element in music:

widget_dict['track'] = mixer.Sound(music[0])
create_widgets(music[0])

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()

