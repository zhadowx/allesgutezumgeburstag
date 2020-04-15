from sound_panel import * 

app = Tk()
app.title("Head First Mix")

mixer = pygame.mixer
mixer.init()

music = ["59264_M_RED_TheDreamDrums.wav", "50848_M_RED_WaveBaseLoop.wav", "50459_M_RED_Nephlimizer.wav", "49119_M_RED_HardBouncer.wav", "45414_M_RED_Trance_Train.wav", "41722__M_RED__happy_freaq.wav", "41312_M_RED_Sonar_Line.wav", "39607__M_RED__trumpet_delay_loop.wav", "39484__M_RED__trance_trumpet_loop.wav", "39147_M_RED_beep_line.wav"]
  
for element in music:
  create_gui(app, mixer, element)

def shutdown():
  mixer.stop()
  app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()