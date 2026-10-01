from microbit import *
import music
import random

MUSIC1 = [
  'A5:2', 'B5:2', 'C6:2', 'A5:2', 'E6:8',
  'A5:2', 'B5:2', 'C6:2', 'G5:2', 'E6:8',
  'A5:2', 'B5:2', 'C6:2', 'D6:2',
  'G5:1', 'G5:2', 'G5:1',
  'G5:2', 'E5:1', 'F5:2', 'G5:1',
  'G5:2', 'G5:1', 'G5:2', 'A5:2', 'G5:8'
]


ALIEN = Image('00000:09090:99999:09990:09090')
JUMP_ALIEN = Image('09090:99999:09990:09090:00000')
FISH = Image('00900:09909:99999:09909:00900')

ANIMATION = (ALIEN, JUMP_ALIEN)

MUSIC_BOX = [MUSIC1]

while True:
  if accelerometer.was_gesture('shake'):
    display.show(ANIMATION, wait=False, loop=True)
  if button_a.was_pressed():
    display.show(FISH)
    music.play(music.BA_DING, wait=False, loop=False)
    sleep(1000)
    display.clear()
  if button_b.was_pressed():
    music.play(random.choice(MUSIC_BOX), wait=False, loop=False)
    display.show(Image.MUSIC_QUAVER)
    sleep(5000)
    display.clear()
  if button_a.was_pressed() and button_b.was_pressed():
    display.show(random.choice.GAMES, wait=False, loop=True)
