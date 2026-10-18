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
  'E6:3', 'D#6:1', 'E6:3', 'G6:6', 'C6:4', 'E6:3', 'D#6:1', 'E6:3', 'G6:10', 'D6:3', 'C#6:1', 'D6:3', 'F6:6', 'B5:4', 'D6:3', 'C#6:1', 'D6:3', 'F6:10', 
  'E6:3', 'D#6:1', 'E6:3', 'G6:6', 'C6:4', 'E6:3', 'D#6:1', 'E6:3', 'G6:10', 'D6:3', 'C#6:1', 'D6:3', 'F6:6', 'B5:4', 'D6:3', 'C#6:1', 'D6:3', 'F6:10', 
  'E6:3', 'D#6:1', 'E6:3', 'G6:6', 'C6:4', 'E6:3', 'D#6:1', 'E6:3', 'G6:10', 'D6:3', 'C#6:1', 'D6:3', 'F6:6', 'B5:4', 'D6:3', 'C#6:1', 'D6:3', 'F6:10'
]


#define minigames
def snake():
  display.scroll('snake!')
  x = 0
  y = 0
  display.clear()
  while True:
    if x == 4 and y == 4:
        music.play(music.POWER_UP, wait=True, loop=False)
        display.clear()
        break
    elif button_a.was_pressed() and x < 4:
      x += 1
      display.set_pixel(x, y, 9)
    elif button_b.was_pressed() and y < 4:
      y += 1
      display.set_pixel(x, y, 9)
    else:
      display.set_pixel(x, y, 9)
      sleep(100)


def reaction():
  display.scroll('reaction!')
  display.scroll(str(3))
  display.scroll(str(2))
  display.scroll(str(1))
  display.scroll('GO!')
  a = 0
  b = 0
  wait_a = False
  while True:
    sleep(3000)
    display.show(Image.TARGET)
    wait_a = True
    a = running_time()
    if button_b.was_pressed() and wait_a == True:
      b_pressed = running_time()
      time = running_time() - b_pressed
      display.scroll(str(time))
    if not button_a.was_pressed() and not button_b.was_pressed():
      display.scroll('you lost')
      break
      
#define images
ALIEN = Image('00000:09090:99999:09990:09090')
JUMP_ALIEN = Image('09090:99999:09990:09090:00000')
FISH = Image('00900:09909:99999:09909:00900')

#animation loop
ANIMATION = (ALIEN, JUMP_ALIEN)

#random commands 
MUSIC_BOX = [MUSIC1, MUSIC2, MUSIC3]
GAMES = [snake, reaction]

#start code
while True:
  #show animation on shake
  if accelerometer.was_gesture('shake'):
    display.show(ANIMATION, wait=False, loop=True) 
    if button_a.is_pressed() and button_b.is_pressed(): #clear when a button is pressed
      display.clear()
      break #break out of loop
    else: 
      display.show(ANIMATION, wait=False, loop=True)      
  #button a and b to play minigames
  if button_a.was_pressed() and button_b.was_pressed():
    music.play(CIRCUS, wait=False, loop=False) 
    random.choice(GAMES)()
    music.stop()
  #button a to feed pet  
  elif button_a.is_pressed() and not button_b.is_pressed(): 
    display.show(FISH)
    music.play(music.BA_DING, wait=False, loop=False) #do not block other commands  
    sleep(500) 
  #button b to play music
  elif button_b.is_pressed() and not button_a.is_pressed():
    music.play(random.choice(MUSIC_BOX), wait=False, loop=False) 
    display.show(Image.MUSIC_QUAVER)
    sleep(5000)
  
    
      
    
      
      
 
