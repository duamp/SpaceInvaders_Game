import pygame
import sys
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
windowX = 450
windowY = 500
window = pygame.display.set_mode((windowX, windowY))
#Create enemy ships
spaceship = pygame.image.load(os.path.join("assets", "ship.png"))
smallShip = pygame.transform.scale(spaceship, (100, 75))
whiteAlien = pygame.image.load(os.path.join("assets", "whiteAlien.png"))
whiteAlienSize = pygame.transform.scale(whiteAlien, (50, 35))
redAlien = pygame.image.load(os.path.join("assets", "redAlien.png"))
redAlienSize = pygame.transform.scale(redAlien, (50, 35))
yellowAlien = pygame.image.load(os.path.join("assets", "yellowAlien.png"))
yellowAlienSize = pygame.transform.scale(yellowAlien, (50, 35))
aliens =[whiteAlienSize,yellowAlienSize,redAlienSize]
arrayE = []

#Create Background
background = pygame.image.load(os.path.join("assets", "stars.jpeg"))
pygame.display.set_caption('Space Invaders')

class player:
    x = 50
    y = 375

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = 5
        self.hitbox = (self.x, self.y, 64,64)

    def draw(self):
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT] and self.x > 0:
            self.x -= self.step
            player.x -= self.step
        if key_input[pygame.K_RIGHT] and self.x < windowX-30:
            self.x += self.step
            player.x += self.step
        window.blit(smallShip, (self.x, self.y))

class enemy:
    iteration = 0

    def __init__(self,x,y,hit,lives):
        self.x = x #30
        self.y = y #0
        self.width = 50
        self.height = 35
        self.stepX = 5
        self.stepY = 10
        self.hitbox = (self.x, self.y, 40,40)
        self.lives = lives
        self.hit = hit

    def draw(self):
        #move enemies
        self.x += self.stepX   
        window.blit(background, (0, 0))
        ship.draw()
        #create enemies
        for i in range(len(arrayE)): 
            if arrayE[i].hit != True:
                if 0 < arrayE[i].x < 400:
                    self.hitbox = (arrayE[i].x, arrayE[i].y, 40,40) 
                elif arrayE[i].x > 400:
                    arrayE[i].x = 399
                    self.stepX = self.stepX*-1
                    arrayE[i].y = arrayE[i].y + self.stepY
                elif arrayE[i].x < 0:    
                    arrayE[i].x = 1
                    self.stepX = self.stepX*-1
                    arrayE[i].y = arrayE[i].y + self.stepY
                window.blit(aliens[arrayE[i].lives], (arrayE[i].x, arrayE[i].y))
                pygame.draw.rect(window,(255,0,0),self.hitbox,2)
                arrayE[i].x = arrayE[i].x + self.stepX 
            
            if((self.hitbox[1] < laser.y < (arrayE[i].y + 40)) and (self.hitbox[0] < laser.x < (arrayE[i].x + 40))):
                    print(self.hitbox[1])
                    print(laser.y)
                    print(arrayE[i].y + 40)
                    arrayE[i].lives += 1
                    laser.y = -1
                    arrayE[i].hit = True

                    
class laser:
    shootGun = False 
    y = 380
    x = player.x+49
    def __init__(self,x):
        self.x = x
        self.y = 380
        self.width = 3
        self.height = 5
        self.step = -10

    def draw(self):
        self.y += self.step
        laser.y += self.step
        pygame.draw.rect(window, (255, 255, 255),(self.x, self.y, 3, 5))
        if(laser.y < 0):
            laser.shootGun = False
            self.y = self.y
            laser.y = 380  

#Constructors
ship = player(50,375,100,75)       
startX = 30
startY = 10
hit = False
lives = 0
for i in range(2):
    for a in range(3):
        arrayE.append((enemy(startX,startY,hit,lives)))
        startX += 50
    startY += 55

while True:
    window.blit(background, (0, 0))
    ship.draw()
    arrayE[i].draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    key = pygame.key.get_pressed()
    if(key[pygame.K_SPACE] or laser.shootGun == True):
        laser.shootGun = True
        Nlaser.draw()
    elif(laser.shootGun == False):
        Nlaser = laser(player.x+49)

    pygame.display.update()
    pygame.time.delay(60)
