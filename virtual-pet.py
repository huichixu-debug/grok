from microbit import *
import music
import random

#define tunes
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


#define minigames
def snake():
  x = 0
  y = 0
  display.set_pixel(x, y, 9)
  if x == 4 and y == 4:
      display.clear()
      x = 0
      y = 0
  if button_a.was_pressed() and x < 4:
      x += 1
  if button_b.was_pressed() and y < 4:
      y += 1
def reaction():
  a = 0
  b = 0
  wait_a = False
  while True:
      if button_a.was_pressed():
        wait_a = True
        wait = 3000
        display.show(Image.TARGET)
        music.play('C6:4', wait=False, loop=False)
        a = running_time()
      if button_b.was_pressed() and wait_a == True:
        b = running_time()
        time = b - a
        display.scroll(time)

    
MOON = Image('00990:09900:09000:09900:00990')
STAR = Image('00900:09990:99999:09990:00900')

#define images
ALIEN = Image('00000:09090:99999:09990:09090')
JUMP_ALIEN = Image('09090:99999:09990:09090:00000')
FISH = Image('00900:09909:99999:09909:00900')

#animation loop
ANIMATION = (ALIEN, JUMP_ALIEN)

#random commands 
MUSIC_BOX = [MUSIC1, MUSIC2, MUSIC3]
GAMES = [snake, reaction]
DREAM = [MOON, STAR, Image.GHOST]

#start code
while True:
  #show animation on shake
  if accelerometer.was_gesture('shake'):
    display.show(ANIMATION, wait=False, loop=True)
  #button a and b to play minigames
  if button_a.was_pressed() and button_b.was_pressed():
    music.play(CIRCUS, wait=True, loop=True)
    random.choice(GAMES)()
  #button a to feed pet  
  elif button_a.is_pressed() and not button_b.is_pressed():
    display.show(FISH)
    music.play(music.BA_DING, wait=False, loop=False)
    sleep(500)
  #button b to play music
  elif button_b.is_pressed() and not button_a.is_pressed():
    music.play(random.choice(MUSIC_BOX), wait=False, loop=False)
    display.show(Image.MUSIC_QUAVER)
    sleep(5000)
  else:
    number = random.randint(1, 3)
    if number == 1:
      display.show(random.choice(DREAM))
    
      
      
 
