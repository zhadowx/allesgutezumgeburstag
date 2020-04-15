import pygame.mixer
from time import sleep

mixer = pygame.mixer
mixer.init()

track = mixer.Sound("50848_M_RED_WaveBaseLoop.wav")
print("Play it LOUD, man!")
track.play(loops = -1)
track.set_volume(0.9)
sleep(2)
print("Softly does it...")
track.set_volume(0.1)
sleep(2)
track.stop()
