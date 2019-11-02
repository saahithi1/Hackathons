# pharma game

import pygame
import gamebox
import random
from pygame.locals import *

camera = gamebox.Camera(800, 750)
display = pygame.display.set_mode((800,750))
image = pygame.image.load("hospital.jpg")

sheet1 = gamebox.load_sprite_sheet(
   "https://3.bp.blogspot.com/-_NVjscKbE7Q/WLB4GtYM6PI/AAAAAAAAIyk/iGm67QmaiV0v0VKNSnG5pzenizWGsbvyQCLcB/s1600/trump_run.png",
   4, 6)

sheet1 = [
sheet1[6],
sheet1[7],
sheet1[8],
sheet1[9],
sheet1[10],
sheet1[11],
]

obstacles = [
gamebox.from_color(camera.right - 100, 585, 'brown', 20, 200),
]

player = gamebox.from_image(camera.right - 750, 50, sheet1[0])
player.x = 50
player.y = 50
touched = []

game_on = False

def tick(keys):
   global game_on
   global score
   global obstacles

   title = gamebox.from_text(camera.right-400, 200, "Day in the Life of a Pharmacist", 60, "blue", True)
   start = gamebox.from_text(camera.right-400, 300, "PRESS THE SPACE BAR TO BEGIN", 30, "blue")
   name = gamebox.from_text(camera.right-400, 450, "Alexa Gomez and Saahithi Budharaju", 30, "blue")
   instructions = gamebox.from_text(camera.right-400, 500,
                                     "Take a tour of the pharmacy to learn what pharmacists do!", 25,
                                     "white")

   camera.clear('black')
   camera.draw(title)
   camera.draw(name)
   camera.draw(instructions)
   camera.draw(start)

   if pygame.K_SPACE in keys:
       game_on = True

   if game_on:
       display.blit(image, (0, 0))
       player.image = "pharm.png"
       camera.draw(player)

       # move down
       if pygame.K_DOWN in keys:
           player.y += 25
       # move up
       if pygame.K_UP in keys:
           player.y -= 25

       # move left
       if pygame.K_LEFT in keys:
           player.x -= 25

       # move right
       if pygame.K_RIGHT in keys:
           player.x += 25

   camera.display()


ticks_per_second = 60

gamebox.timer_loop(ticks_per_second, tick)






