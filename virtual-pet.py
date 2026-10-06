from microbit import *
import music
import random

MUSIC1 = [
  'A5:3', 'B5:3', 'C6:3', 'A5:3', 'E6:12',
  'A5:3', 'B5:3', 'C6:3', 'G5:3', 'E6:12',
  'A5:3', 'B5:3', 'C6:3', 'D6:3',
  'G5:2', 'G5:2', 'G5:2',
  'G5:3', 'E5:2', 'F5:2', 'G5:2',
  'G5:3', 'G5:2', 'G5:4', 'A5:3', 'G5:9'
]

MUSIC2 = [
  'A6:4', 'G6:4', 'F6:4', 'E6:6', 'E6:2', 'r1', 'E6:2', 'r1', 'E6:2', 'r1', 'D6:6', 'E6:2', 'G6:2', 'B5:2', 'C6:4', 'C6:1', 'r1', 'E6:2', 'E6:2', 'E6:2', 'E6:2', 'E6:2', 'E6:2', 'E6:2', 'D6:6', 'E6:2', 'G6:2', 'B5:2', 'C6:4', 'C6:2'
]

MUSIC3 = [
  'r2', 'E6:2', 'r1','E6:2', 'r1','E6:2', 'r1','E6:2','E6:2','E6:2','E6:2','G6:2','A6:2','G6:4','r2', 'D6:2', 'r1','D6:2', 'r1','D6:2', 'r1','D6:2','D6:2','D6:2','D6:2','G6:2','A6:2','G6:4', 'r2', 'E6:2', 'r1','E6:2', 'r1','E6:2', 'r1','E6:2','E6:2','E6:2','E6:2','G6:2','A6:2','G6:4', 'D6:4', 'E6:4', 'D6:2', 'C6:2', 'A5:2', 'G5:2', 'D6:4', 'E6:4', 'D6:2', 'C6:2', 'C6:4'  
]

CIRCUS = [
  'E6:3', 'D#6:1', 'E6:3', 'G6:6', 'C6:4', 'E6:3', 'D#6:1', 'E6:3', 'G6:10', 'D6:3', 'C#6:1', 'D6:3', 'F6:6', 'B5:4', 'D6:3', 'C#6:1', 'D6:3', 'F6:10'
]
ALIEN = Image('00000:09090:99999:09990:09090')
JUMP_ALIEN = Image('09090:99999:09990:09090:00000')
FISH = Image('00900:09909:99999:09909:00900')

ANIMATION = (ALIEN, JUMP_ALIEN)

MUSIC_BOX = [MUSIC1, MUSIC2, MUSIC3]

last_a = 0
last_b = 0

while True:
  if accelerometer.was_gesture('shake'):
    display.show(ANIMATION, wait=False, loop=True)
    last_a = running_time()
    last_b = running_time()
  if abs(last_a - last_b) < 1000 and abs(last_a - last_b) != 0:
    display.show(Image.HAPPY)
    music.play(CIRCUS, wait=False, loop=True)
  elif button_a.is_pressed() and not button_b.is_pressed():
    display.show(FISH)
    music.play(music.BA_DING, wait=False, loop=False)
    sleep(500)
  elif button_b.is_pressed() and not button_a.is_pressed():
    music.play(random.choice(MUSIC_BOX), wait=False, loop=False)
    display.show(Image.MUSIC_QUAVER)
    sleep(5000)
    
      
      
 
