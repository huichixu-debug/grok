
from microbit import *
import music
import random

MUSIC1 = [
  'A5:1, B5:1, C5:1, A5:1, E5:4, A5:1, B5:1, C5:1, A5:1, E5:4, A5:1, B5:1, C5:1, D5:1, G4:1, G4:1, G4:1, G4:1, E4:1, F4:1, G4:1, G4:2, G4:1, G4:1, A4:1, G4:4' 
]
MUSIC2 = [
  'E5:1, E5:1, E5:4'
]
MUSIC3 = [
  'C4:1, D4:1, E4:1'
]

ALIEN = Image('00000:09090:99999:09990:09090')
JUMP_ALIEN = Image('09090:99999:09990:09090:00000')
FISH = Image('00900:09909:99999:09909:00900')

ANIMATION = (ALIEN, JUMP_ALIEN)

MUSIC_BOX = [MUSIC1, MUSIC2, MUSIC3]

while True:
  if button_a.was_pressed():
    display.show(FISH)
    music.play(music.BA_DING, wait=False, loop=True)
    sleep(1000)
    display.clear()
  elif accelerometer.was_gesture('shake'):
    display.show(ANIMATION, wait=True, loop=True)
  elif button_b.was_pressed():
    music.play(random.choice.MUSIC_BOX, wait=False, loop=True)
    display.show(Image.MUSIC_QUAVER)
    sleep(1000)
    display.clear()
  elif button_a.was_pressed() and button_b.was_pressed():
    display.show(random.choice.GAMES, wait=False, loop=True)
