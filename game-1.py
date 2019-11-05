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
# patient room
gamebox.from_color(625, 315, 'green', 20, 20),
# pharmacy room
gamebox.from_color(295, 630, 'green', 20, 20),
gamebox.from_color(340, 255, 'green', 20, 20),
gamebox.from_color(135, 375, 'green', 20, 20),
]


player = gamebox.from_image(camera.right - 750, 50, sheet1[0])
player.x = 50
player.y = 50

game_on = False
count = 0

def tick(keys):
   global game_on
   global obstacles
   global count


   title = gamebox.from_text(camera.right-400, 200, "Day in the Life of a Pharmacist", 60, "blue", True)
   start = gamebox.from_text(camera.right-400, 300, "PRESS THE SPACE BAR TO BEGIN", 30, "blue")
   name = gamebox.from_text(camera.right-400, 450, "Alexa Gomez and Saahithi Budharaju", 30, "blue")
   instructions = gamebox.from_text(camera.right-400, 500,
                                     "Take a tour of the pharmacy to learn what pharmacists do!", 25,
                                     "white")
   welcome = gamebox.from_text(125,100, "Welcome to the hospital!", 20, "blue")
   welcome2 = gamebox.from_text(125,125, "Navigate around to the green blocks", 20, "blue")
   welcome3 = gamebox.from_text(125,150, "to learn about a day in my life.", 20, "blue")


   camera.clear('black')
   camera.draw(title)
   camera.draw(name)
   camera.draw(instructions)
   camera.draw(start)

   if pygame.K_SPACE in keys:
       game_on = True

   if game_on:
       player.image = "pharm.png"

       if count == 0:
           player.scale_by(0.6)
           count+=1


       display.blit(image, (0, 0))
       camera.draw(player)
       if player.x == (camera.right -750) and player.y == 50:
           camera.draw(welcome)
           camera.draw(welcome2)
           camera.draw(welcome3)
       for obs in obstacles:
           camera.draw(obs)

       if player.left < camera.left:
            player.x = 15
       if player.right > camera.right:
            player.x = 785
       if player.top < camera.top:
           player.y = 15
       if player.bottom > camera.bottom:
           player.y = 735

       for obs in obstacles:
           if player.touches(obs):
               # pharm room
               if obs == obstacles[1]:
                   texts = [
                       gamebox.from_text(125, 50, "One of my biggest responsibilities", 20, "blue"),
                       gamebox.from_text(125, 75, "is to safely and accurately", 20, "blue"),
                       gamebox.from_text(125, 100, "distribute medication to patients. I", 20, "blue"),
                       gamebox.from_text(125, 125, "need to make sure they get the right", 20, "blue"),
                       gamebox.from_text(125, 150, "prescription with the right dose.", 20, "blue")
                   ]
                   for text in texts:
                       camera.draw(text)
               # patient room
               if obs == obstacles[0]:
                   texts = [
                       gamebox.from_text(125, 50, "Sometimes I screen patients for", 20, "blue"),
                       gamebox.from_text(125, 75, "major diseases and administer", 20, "blue"),
                       gamebox.from_text(125, 100, "vaccinations like the flu shot,", 20, "blue"),
                       gamebox.from_text(125, 125, "but this varies from state to state.", 20, "blue"),
                       gamebox.from_text(125, 150, "prescription with the right dose.", 20, "blue")
                   ]
                   for text in texts:
                       camera.draw(text)

                # patient and doc room
               if obs == obstacles[2]:
                   texts = [
                       gamebox.from_text(125, 50, "At the hospital I can provide targeted", 20, "blue"),
                       gamebox.from_text(125, 75, " behavioral counseling to help", 20, "blue"),
                       gamebox.from_text(125, 100, "patients manage their medication", 20, "blue"),
                       gamebox.from_text(125, 125, "use. I can support struggling", 20, "blue"),
                       gamebox.from_text(125, 150, "with addiction and recovery.", 20, "blue")
                   ]
                   for text in texts:
                       camera.draw(text)


               # doctor room
               if obs == obstacles[3]:
                   texts = [
                   gamebox.from_text(125, 50, "I go on rounds with doctors and", 20, "blue"),
                   gamebox.from_text(125, 75, "nurses to collect medical and drug", 20, "blue"),
                   gamebox.from_text(125, 100, "histories from patients and", 20, "blue"),
                   gamebox.from_text(125, 125, "educate them about managing their", 20, "blue"),
                   gamebox.from_text(125, 150, "medicine. I can make suggestions", 20, "blue"),
                   gamebox.from_text(125, 175, "for treatment options based on", 20, "blue"),
                   gamebox.from_text(125, 200, "my knowledge of drug interactions.", 20, "blue")
                   ]
                   for text in texts:
                       camera.draw(text)


       # move down
       if pygame.K_DOWN in keys:
           player.y += 15

       # move up
       if pygame.K_UP in keys:
           player.y -= 15

       # move left
       if pygame.K_LEFT in keys:
           player.x -= 15

       # move right
       if pygame.K_RIGHT in keys:
           player.x += 15

   camera.display()


ticks_per_second = 60

gamebox.timer_loop(ticks_per_second, tick)






