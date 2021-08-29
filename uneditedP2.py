import pygame
import sys
import os

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
        self.step = 15
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
    collision = False
    iteration = 0

    def __init__(self,x,y,width,height):
        self.x = 30
        self.y = 0
        self.width = width
        self.height = height
        self.stepX = 2
        self.stepY = 3
        self.hitbox = (self.x, self.y, 40,40)
        self.health = 3
        self.collision = False

    def draw(self):
        #move enemies
        self.x += self.stepX
        if self.x > 70 or self.x < 0:
            self.stepX = self.stepX*-1
            self.y += self.stepY
    
        #create enemies
        for i in range(7):
            for a in range(3): 
                x = self.x + 55*i     
                y = self.y + 55*a     
                if (enemy.collision == False):
                    window.blit(aliens[enemy.iteration], (x, y))
                    pygame.draw.rect(window,(255,0,0),self.hitbox,2)
                    self.hitbox = (x, y, 40,40)
                enemy.collision = False

                if((self.hitbox[3] < laser.y < (y + 40)) and (self.hitbox[2] < laser.x < (x + 40))):
                    print(x,y)
                    enemy.iteration +=1
                    laser.y = -1
                    enemy.collision = True
                    return

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
Nenemy = enemy(100,100,50,35)

while True:
    window.blit(background, (0, 0))
    ship.draw()
    Nenemy.draw()
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
