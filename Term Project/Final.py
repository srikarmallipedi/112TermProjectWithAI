    
import pygame
import random
from random import randint
from os import path
import math
import time
def main():
    #This is all data we need in order to set up pygames display as well as 
    #blit our sprites for animation The 4 value tuples contain the points of
    #the actual sprites we need to blit for our game
    WIDTH0=923
    HEIGHT0=547
    WIDTH = 774
    HEIGHT = 438
    FPS = 30
    playerScore=0
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255) 
    BROWN=(165,42,42)
    PINK=(255,192,203)
    RED=(255,0,0)
    PURPLE=(204,51,153)
    LIGHTGREEN=(102,255,102)
    GREEN=(0,255,0)
    DARKGREEN=()
    bossHealth=50
    cupHeadHealth=5
    DARKPURPLE=(51,0,25)
    distanceFromBeginning=0
    pygame.init()
    pygame.mixer.init()
    screen0=pygame.display.set_mode((WIDTH0,HEIGHT0))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    images=path.join(path.dirname(__file__), "sprites")
    BulletTypes=["Peashooter", "Spread", "Turners"]
    movement=pygame.image.load(path.join(images, "SpriteSheet.png")).convert()
    boss=pygame.image.load(path.join(images, "DevilWife.png")).convert()
    overWorldWalking=pygame.image.load(path.join(images, "OverWorldWalk.png")).convert()
    TheOverWorld=pygame.image.load(path.join(images, "overWorld.png")).convert()
    platforms=pygame.image.load(path.join(images,"platforms.png")).convert()
    lair=pygame.image.load(path.join(images,"EvilLair.png")).convert()
    WorldWalkUp=[]
    WorldWalkDown=[]
    WorldWalkRight=[]
    WorldWalkLeft=[]
    WorldWalkUpLeft=[]
    WorldWalkUpRight=[]
    WorldWalkDownRight=[]
    WorldWalkDownLeft=[]
    PlatformPull=(127,145,100,50)
    SP_StandStill=(324,0,50,45)
    SP_ListRun=[(631,234,44,38), (675,234,44,37),(354,234,54,41),
    (408,234,50,37),(538,234,45,40),(583,234,46,40)]
    SP_WalkUp=[(434,20,66,84),(535,16,66,84),(638,13,66,91),(748,15,59,91),
    (846,10,59,96),(949,16,69,85),(1046,15,66,85),(1153,16,67,91),(1256,15,61,91)]
    SP_WalkUpRight=[(423,124,58,91),(534,123,60,86),(637,123,61,92),
    (736,123,71,92),(843,124,60,88),(948,130,60,80),(1051,123,60,92),
    (1154,126,61,90),(1263,123,54,99)]
    SP_WalkRight=[(430,350,66,100),(534,350,66,94),(638,350,66,100),
    (742,350,66,100),(843,350,69,100),(947,350,69,100),(1051,350,69,100),
    (1155,350,69,100),(1259,350,69,100),(1363,350,69,100)]
    SP_OverWorldStill=[(327,581,61,96)]
    SP_WalkDownRight=[(430,457,68,105),(534,457,68,105),(638,457,68,105),
    (742,457,68,105),(846,457,68,105),(950,457,68,105),
    (1054,457,68,105),(1158,457,68,105),(1262,457,68,105),(1366,457,68,105)]
    SP_WalkDown=[(18,687,66,97),(127,684,60,104),
    (232,684,65,104),(335,684,60,98),(438,687,60,90),(535,691,67,92),
    (643,681,54,104),(743,684,66,106),(850,679,56,106),(949,679,59,112)]
    BLITWALKRIGHT=[]
    BLITWALKLEFT=[]
    BLITWALKDOWN=[]
    BLITWALKUP=[]
    BLITWALKUPRIGHT=[]
    BLITWALKDOWNRIGHT=[]
    BLITWALKUPLEFT=[]
    BLITWALKDOWNLEFT=[]
    BLITOVERWORLDSTILL=[]
    BLITRUNRIGHT=[]
    BLITSTILL=[]
    #these loops construct lists containing 
    #blitted images with the appropriate colorkey and 
    #formatt so that we can animate our character
    #this concept comes from the kids can code pygame tutorial
    # https://www.youtube.com/watch?v=_y5U8tB36Vk, however the code is different
    for tup in SP_WalkRight:
        temp=pygame.Surface((tup[2],tup[3]))
        temp.blit(overWorldWalking, (0,0),(tup[0],tup[1],tup[2],tup[3]))
        final=pygame.transform.scale(temp, (int(tup[2]*0.65), int(tup[3]*0.65)))
        final.set_colorkey(GREEN)
        BLITWALKRIGHT.append(final)
    for tup in SP_WalkDown:
        temp=pygame.Surface((tup[2],tup[3]))
        temp.blit(overWorldWalking, (0,0),(tup[0],tup[1],tup[2],tup[3]))
        final=pygame.transform.scale(temp, (int(tup[2]*0.65), int(tup[3]*0.65)))
        final.set_colorkey(GREEN)
        BLITWALKDOWN.append(final)
    for tup in SP_WalkUpRight:
        temp=pygame.Surface((tup[2],tup[3]))
        temp.blit(overWorldWalking, (0,0),(tup[0],tup[1],tup[2],tup[3]))
        final=pygame.transform.scale(temp, (int(tup[2]*0.65), int(tup[3]*0.65)))
        final.set_colorkey(GREEN)
        BLITWALKUPRIGHT.append(final)
    for tup in SP_WalkUp:
        temp=pygame.Surface((tup[2],tup[3]))
        temp.blit(overWorldWalking, (0,0),(tup[0],tup[1],tup[2],tup[3]))
        final=pygame.transform.scale(temp, (int(tup[2]*0.65), int(tup[3]*0.65)))
        final.set_colorkey(GREEN)
        BLITWALKUP.append(final)
    for tup in SP_WalkDownRight:
        temp=pygame.Surface((tup[2],tup[3]))
        temp.blit(overWorldWalking, (0,0),(tup[0],tup[1],tup[2],tup[3]))
        final=pygame.transform.scale(temp, (int(tup[2]*0.65), int(tup[3]*0.65)))
        final.set_colorkey(GREEN)
        BLITWALKDOWNRIGHT.append(final)
    for tup in SP_OverWorldStill:
        temp=pygame.Surface((tup[2],tup[3]))
        temp.blit(overWorldWalking, (0,0),(tup[0],tup[1],tup[2],tup[3]))
        final=pygame.transform.scale(temp, (int(tup[2]*0.65), int(tup[3]*0.65)))
        final.set_colorkey(GREEN)
        BLITOVERWORLDSTILL.append(final)
    for elem in BLITWALKDOWNRIGHT:
        BLITWALKDOWNLEFT.append(pygame.transform.flip(elem, True, False))
    for elem in BLITWALKRIGHT:
        BLITWALKLEFT.append(pygame.transform.flip(elem, True, False))
    for elem in BLITWALKUPRIGHT:
        BLITWALKUPLEFT.append(pygame.transform.flip(elem, True, False))
    playerX=0
    for tup in SP_ListRun:
        temp=pygame.Surface((tup[2],tup[3]))
        temp.blit(movement, (0,0),(tup[0],tup[1],tup[2],tup[3]))
        final=pygame.transform.scale(temp, (int(1.5*tup[2]), int(1.5*tup[3])))
        final.set_colorkey(BLACK)
        BLITRUNRIGHT.append(final)
    BLITRUNLEFT=[]
    for drawing in BLITRUNRIGHT:
        BLITRUNLEFT.append(pygame.transform.flip(drawing, True, False))
    BLITSTILL=[]
    rightStill=pygame.Surface((SP_StandStill[2], SP_StandStill[3]))
    rightStill.blit(movement, (0,0), (SP_StandStill[0], SP_StandStill[1],
    SP_StandStill[2], SP_StandStill[3]))
    stillR=pygame.transform.scale(temp, (int(1.5*SP_StandStill[2]),
     int(1.5*SP_StandStill[3])))
    stillR.set_colorkey(BLACK)
    BLITSTILL.append(stillR)
    stillL=pygame.transform.flip(stillR, True, False)
    BLITSTILL.append(stillL)
    enemyImg=pygame.image.load(path.join(images, "FlowerEnemy1.png")).convert()
    backGround=pygame.image.load(path.join(images, "background.png")).convert()
    startScreenImage=pygame.image.load(path.join(images, "StartImage.png")).convert()
    DuneBackground=pygame.image.load(path.join(images, "DuneBackground.png")).convert()
    #this concept comes from the kids can code pygame tutorial
    # https://www.youtube.com/watch?v=_y5U8tB36Vk
    def pullImage(overall,x,y,width,height):
        img=pygame.Surface((width, height))
        img.blit(overall, (0,0),(x,y,width,height))
        return img
    #to be later implemented for falling gravity and jumping
    vector=pygame.math.Vector2
    #the plaayer class, controls the player and such
    class cupHeadPlayer(pygame.sprite.Sprite):
        #the init function contains a variety of things
        def __init__(self,spriteGroup):
            pygame.sprite.Sprite.__init__(self)
            #the image i used from online, is animated so that 
            #the movement is more robust
            img=pygame.Surface((SP_StandStill[2],SP_StandStill[3]))
            img.blit(movement, (0,0),   (SP_StandStill[0],SP_StandStill[1],SP_StandStill[2],SP_StandStill[3]))
            self.image=pygame.transform.scale(img, (int(1.5*SP_StandStill[2]), int(1.5*SP_StandStill[3])))
            #self.image.set_colorkey(BLACK)
            # print(movement)
            # print(self.image)
            self.radius=10
            self.spriteGroup=spriteGroup
            #removes all black from the picture
            self.image.set_colorkey(BLACK)
            self.gun=0
            self.dirFacing=True
            self.rect=self.image.get_rect()
            self.rect.bottom=HEIGHT-10
            self.position=vector(WIDTH/6, self.rect.bottom-25)
            self.centery=self.rect.bottom-25
            self.speedx=0
            self.isMove=False
            self.isJumping=False
            self.still=not self.isJumping and not self.isMove
            self.frame=0
            self.sinceLast=0
            self.count=0
            self.type="Peashooter"
            self.distanceFromBeginning=0
        #the acceleration vector I will later use for gravity
        #this implementation of movement into vectors was taken from                     
        #https://www.youtube.com/watch?v=_y5U8tB36Vk, Kids Who can code 
        #a youtube series dedicated to teaching pygame
            self.velocity=vector(0,0)
            self.acceleration=vector(0,0)
        def update(self):
            #self.movingSprite()
            playerX=self.rect.x
            self.acceleration=vector(0,0.68)
            self.velocity.x=0
            keystate=pygame.key.get_pressed()
            currentTime=pygame.time.get_ticks()
            if keystate[pygame.K_LEFT]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITRUNLEFT)
                    bottom=self.rect.bottom
                    self.image=BLITRUNLEFT[self.frame]
                    self.rect.bottom=bottom
                    self.dirFacing=False
                self.velocity.x-=7
                self.distanceFromBeginning+=self.velocity.x
            elif keystate[pygame.K_RIGHT]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITRUNRIGHT)
                    bottom=self.rect.bottom
                    self.image=BLITRUNRIGHT[self.frame]
                    self.rect.bottom=bottom
                    self.dirFacing=True
                self.velocity.x+=7
                self.distanceFromBeginning+=self.velocity.x
            elif self.dirFacing:
                bott=self.rect.bottom
                img=pygame.Surface((SP_StandStill[2],SP_StandStill[3]))
                img.blit(movement, (0,0),   (SP_StandStill[0],SP_StandStill[1],SP_StandStill[2],SP_StandStill[3]))
                self.image=pygame.transform.scale(img, 
                (int(1.5*SP_StandStill[2]), int(1.5*SP_StandStill[3])))
                self.image.set_colorkey(BLACK)
                self.rect.bottom=bott
            elif not self.dirFacing:
                bott=self.rect.bottom
                img=pygame.Surface((SP_StandStill[2],SP_StandStill[3]))
                img.blit(movement, (0,0),   (SP_StandStill[0],SP_StandStill[1],SP_StandStill[2],SP_StandStill[3]))
                img.set_colorkey(BLACK)
                temp=pygame.transform.scale(img, (int(1.5*SP_StandStill[2]),
                 int(1.5*SP_StandStill[3])))
                self.image=pygame.transform.flip(temp,True,False)
                self.rect.bottom=bott
            #kinematics taken from https://www.youtube.com/watch?v=_y5U8tB36Vk 
            self.velocity+=self.acceleration
            self.position+=self.velocity+0.5*self.acceleration
            self.rect.x+=self.velocity.x
            self.rect.y+=self.velocity.y
            self.rect.midbottom = self.position
        def shoot(self):
            if(BulletTypes[self.gun]=="Peashooter"):
                #the regular basic shooting concept was also taken from
                #https://www.youtube.com/watch?v=_y5U8tB36Vk essentially,
                # lines 236-240 were taken
                if(self.dirFacing):
                    bullet = Shot(1,self.position.x+25, self.position.y-30)
                else:
                    bullet=Shot(-1,self.position.x-23, self.position.y-26)
                self.spriteGroup.add(bullet)
                bullets1.add(bullet)
            #a container that holds different bullet types
            elif(BulletTypes[self.gun]=="Spread"):
                #the spread gun counts as 3 sprites so three sprites
                # must be added
                if(self.dirFacing):
                    temp1=SpreadShot("top",1, 
                    self.position.x+25,self.position.y-30)
                    temp2=SpreadShot("mid",1, 
                    self.position.x+25,self.position.y-30)
                    temp3=SpreadShot("down",1, 
                    self.position.x+25,self.position.y-30)
                    bullets2.add(temp1)
                    bullets2.add(temp2)
                    bullets2.add(temp3)
                    self.spriteGroup.add(temp1)
                    self.spriteGroup.add(temp2)
                    self.spriteGroup.add(temp3)
                else:
                    temp1=SpreadShot("top",-1, self.position.x-23,
                                    self.position.y-18)
                    temp2=SpreadShot("mid",-1, self.position.x-23,
                                    self.position.y-18)
                    temp3=SpreadShot("down",-1, 
                                    self.position.x-23,self.position.y-18)
                    bullets2.add(temp1)
                    bullets2.add(temp2)
                    bullets2.add(temp3)
                    self.spriteGroup.add(temp1)
                    self.spriteGroup.add(temp2)
                    self.spriteGroup.add(temp3)
            #a more complex gun type
            elif(BulletTypes[self.gun]=="Turners"):
                if(self.dirFacing):
                    bullet=BoomerangShot(1,self.position.x+30,
                                        self.position.y-18)
                else:
                    bullet=BoomerangShot(-1,self.position.x-23,
                                        self.position.y-18)
                bullets3.add(bullet)
                self.spriteGroup.add(bullet)
        def jump(self):
            self.rect.x+=1
            #taken from https://www.youtube.com/watch?v=_y5U8tB36Vk same one
            coll=pygame.sprite.spritecollide(self, landsLevel1, False)
            if coll:
                self.velocity.y-=10
    #the class that deals with the overworld 
    class OverWorldPlayer(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image=BLITOVERWORLDSTILL[0]
            self.radius=45
            self.rect=self.image.get_rect()
            self.acceleration=vector(0,0)
            self.velocity=vector(0,0)
            self.rect.bottom=HEIGHT-300
            self.position=vector(x, y)
            self.centery=self.rect.bottom-50
            self.speedx=0
            self.sinceLast=0
            self.frame=-1
            self.acceleration=vector(0,0)
        def setPos(xPoint, yPoint):
            self.position=vector(xPoint,yPoint)
        #this sprite moves all 8 directions so must be animated appropriately
        def update(self):
            self.velocity.x=0
            self.velocity.y=0
            currentTime=pygame.time.get_ticks()
            keystate=pygame.key.get_pressed()
            if keystate[pygame.K_LEFT] and keystate[pygame.K_UP]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITWALKUPLEFT)
                    bottom=self.rect.bottom
                    self.image=BLITWALKUPLEFT[self.frame]
                    self.rect.bottom=bottom
                self.velocity.x-=3
                self.velocity.y-=3
            elif keystate[pygame.K_LEFT] and keystate[pygame.K_DOWN]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITWALKDOWNLEFT)
                    bottom=self.rect.bottom
                    self.image=BLITWALKDOWNLEFT[self.frame]
                    self.rect.bottom=bottom
                self.velocity.x-=4
                self.velocity.y+=4
            elif keystate[pygame.K_RIGHT] and keystate[pygame.K_DOWN]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITWALKDOWNRIGHT)
                    bottom=self.rect.bottom
                    self.image=BLITWALKDOWNRIGHT[self.frame]
                    self.rect.bottom=bottom
                self.velocity.x+=4
                self.velocity.y+=4
            elif keystate[pygame.K_RIGHT] and keystate[pygame.K_UP]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITWALKUPRIGHT)
                    bottom=self.rect.bottom
                    self.image=BLITWALKUPRIGHT[self.frame]
                    self.rect.bottom=bottom
                self.velocity.x+=4
                self.velocity.y-=4
            elif keystate[pygame.K_RIGHT]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITWALKRIGHT)
                    bottom=self.rect.bottom
                    self.image=BLITWALKRIGHT[self.frame]
                    self.rect.bottom=bottom
                self.velocity.x+=5
            elif keystate[pygame.K_LEFT]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITWALKLEFT)
                    bottom=self.rect.bottom
                    self.image=BLITWALKLEFT[self.frame]
                    self.rect.bottom=bottom
                self.velocity.x-=5
            elif keystate[pygame.K_UP]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITWALKUP)
                    bottom=self.rect.bottom
                    self.image=BLITWALKUP[self.frame]
                    self.rect.bottom=bottom
                self.velocity.y-=5
            elif keystate[pygame.K_DOWN]:
                if currentTime-self.sinceLast>1:
                    self.sinceLast=currentTime
                    self.frame+=1
                    self.frame=self.frame%len(BLITWALKDOWN)
                    bottom=self.rect.bottom
                    self.image=BLITWALKDOWN[self.frame]
                    self.rect.bottom=bottom
                self.velocity.y+=5
            else:
                self.image=BLITOVERWORLDSTILL[0]
            self.rect.x+=self.velocity.x
            self.rect.y+=self.velocity.y
    #the enemy class 
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image= enemyImg
            #print(self.image)
            self.radius=17
            self.image.set_colorkey(WHITE)
            self.rect=self.image.get_rect()
            self.rect.x = randint(400, WIDTH+400)
            self.rect.bottom=HEIGHT-10
            #Slightly slower than our player
            self.speedx=-3
        def update(self):
            #ensures that they don't ever get fast
            if(abs(self.speedx)>=9):
                self.speedx=0.33*self.speedx
            if(self.rect.left<=0):
                self.speedx*=-1
            if(self.rect.left>=WIDTH+100):
                self.speedx*=-1
            self.rect.x+=self.speedx
   #the boss employs AI and random patterns to defeat the player
    class Boss(pygame.sprite.Sprite):
        def __init__(self, x,y):    
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.transform.scale(boss,(x,y))
            self.image.set_colorkey(BLACK)
            self.rect=self.image.get_rect()
            self.rect.centerx = WIDTH-50
            self.rect.centery=HEIGHT-130
            self.rect.bottom=(HEIGHT-130)+50
            self.rect.top=(HEIGHT-130)-50
            self.speedy=-15
            self.initialize=0
            self.timer1=0
            self.timer2=0
            self.timer3=0
        def update(self):
            current=pygame.time.get_ticks()
            if abs(self.timer1-current)>=900:
                self.timer1=current
                self.bossShoot()
            if abs(self.timer2-current)>=1300:
                self.timer2=current
                self.meteorAttack()
            if abs(self.timer3-current)>=2000:
                self.timer3=current
                self.specialAttack()
            if(abs(self.speedy)>=18):
                self.speedy*=0.33
            if self.rect.y<=30:
                self.speedy*=-1
            elif self.rect.y>=240:
                self.speedy*=-1
            self.rect.y+=self.speedy
        #regular horizontal attack
        def bossShoot(self):
            y=random.randrange(self.rect.top,self.rect.bottom)
            doop=BossShot(y, self.rect.left)
            enemyShots.add(doop)
            all_spritesBoss.add(doop)
       #vertical attack
        def meteorAttack(self):
            x=random.randrange(0,WIDTH)
            boop=Meteor(x,0)
            enemyShots.add(boop)
            all_spritesBoss.add(boop)
        #ai attack that uses vector and players position to send attack
        def specialAttack(self):
            soop=AIAttack(bossPlayer.rect.left, bossPlayer.rect.bottom)
            enemyShots.add(soop)
            all_spritesBoss.add(soop)
    #AI attack that knows player information
    class AIAttack(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.Surface((10, 10))
            self.image.fill(GREEN)
            self.rect=self.image.get_rect()
            self.rect.x=WIDTH-60
            self.rect.y=50
            self.slopex=x
            self.slopey=y
            self.radius=5
            self.deltax=self.rect.x-x
            self.deltay=self.rect.y-y
            self.timeFactor=43
            self.velocity=vector(0,0)
            self.velocity.x=self.deltax/self.timeFactor
            self.velocity.y=self.deltay/self.timeFactor
        def update(self):
            if self.rect.bottom>=HEIGHT:
                self.kill()
            elif self.rect.x<=0:
                self.kill()
            self.rect.x-=self.velocity.x
            self.rect.y-=self.velocity.y
    class BossShot(pygame.sprite.Sprite):
        def __init__(self, point, left):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.Surface((16, 9))
            self.image.fill(PINK)
            self.rect=self.image.get_rect()
            self.rect.y=point
            self.rect.x=left
            self.radius=8
            self.speedx=-15
            self.speedy=0
            self.distanceTraveled=0
        def update(self):
            if self.rect.left<=playerX-50 or self.rect.bottom>=HEIGHT:
                self.kill()
            elif self.rect.top<=200 and (abs(playerX-self.rect.left)<=9):
                self.speedx=0
                self.speedy=15
            self.rect.y+=self.speedy
            self.rect.x+=self.speedx
    #special vertical attack
    class Meteor(pygame.sprite.Sprite):
        def __init__(self,x,default):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.Surface((9, 16))
            self.image.fill(RED)
            self.rect=self.image.get_rect()
            self.rect.y=0
            self.rect.x=x
            self.radius=9
            self.speedx=0
            self.speedy=15
            self.distanceTraveled=0
        def update(self):
            if self.rect.y>=HEIGHT:
                self.kill()
            self.rect.y+=self.speedy
            self.rect.x+=self.speedx
    #the bullets the player has, spread regular and boomerang
    # for maximum effectiveness
    class Shot(pygame.sprite.Sprite):
        def __init__(self,dir,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10,10))
            self.image.fill(BLUE)
            self.rect = self.image.get_rect()
            self.rect.bottom  = y
            self.rect.centerx = x
            self.rect.y=y
            self.speed=10
            self.dir=dir 
        def update(self):
            self.image.fill(BLUE)
            self.rect.x +=self.speed*self.dir
            if self.rect.x>=WIDTH or self.rect.x<=0:
                self.kill()
    class SpreadShot(pygame.sprite.Sprite):
        def __init__(self,orient,dir,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10,15))
            self.image.fill(RED)
            self.originalX=x
            self.rect = self.image.get_rect()
            self.orient=orient
            self.rect.bottom  = y
            self.rect.centerx = x
            self.speed=16
            self.dir=dir
        def update(self):
            if self.orient=="top":
                self.rect.y+=5*self.dir
                self.rect.x+=self.speed*self.dir
            elif self.orient=="mid":
                self.rect.x+=self.speed*self.dir
            elif self.orient=="down":
                self.rect.y-=5*self.dir
                self.rect.x+=self.speed*self.dir
            if abs(self.rect.x-self.originalX)>=200:
                self.kill()
    class BoomerangShot(pygame.sprite.Sprite):
        def __init__(self,dir,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((17,10))
            self.image.fill(LIGHTGREEN)
            self.originalX=x
            self.current=pygame.time.get_ticks()
            self.shouldTurn=True
            self.rect = self.image.get_rect()
            self.rect.bottom  = y
            self.rect.centerx = x
            self.speed=9
            self.dir=dir
        def update(self):
            if(pygame.time.get_ticks()-self.current<=500):
                self.rect.x+=self.speed*self.dir   
            else:
                self.rect.y-=0.2
                self.rect.x-=self.speed*self.dir
            if self.rect.centerx>=WIDTH:
                self.kill()
    #level class that holds the level, keeps track if it has been beaten or not
    class Level(pygame.sprite.Sprite):
        def __init__(self, x,y,r,beat,levelName):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.Surface((30,30))
            self.rect=self.image.get_rect()
            self.image.set_colorkey(BLACK)
            self.radius=r
            self.beat=beat
            self.color=RED
            self.rect.bottom=y+self.radius
            self.rect.left=x-self.radius
            self.x=x
            self.y=y
            self.levelName=levelName
        def getLevelName(self):
            return self.levelName
        def update(self):
            if self.beat:
                self.color=BLUE
        def getAttributes(self):
            return (self.x,self.y,self.radius,self.color)
    #land concept, contains platforms and ground, taken from same place as before
    
    class Land(pygame.sprite.Sprite):
        def __init__(self, x,y, width, height):
            pygame.sprite.Sprite.__init__(self)
            temp=pygame.Surface((width, height))
            temp.blit(platforms, (0,0),(PlatformPull[0],PlatformPull[1],
            PlatformPull[2],PlatformPull[3]))
            self.image=pygame.transform.scale(temp,(width,height))
            self.rect = self.image.get_rect()
            self.rect.x=x
            self.rect.y=y
        def __eq__(self, other):
            return self.rect.x==other.rect.x and self.rect.y==other.rect.y
        def __hash__(self):
            return hash((self.rect.x,self.rect.y))
    #most important container in pygame, the actual lists
    # of sprites that the user sees when playing the game. 
    #They are what the user essentially interacts with.
    all_spritesLevel1 = pygame.sprite.Group()
    all_spritesBoss=pygame.sprite.Group()
    all_spritesLevel2=pygame.sprite.Group()
    landsLevel2=pygame.sprite.Group()
    landsBoss=pygame.sprite.Group()
    # playerBoss=cupHeadPlayer()
    # all_spritesBoss.add(playerBoss)
    theWife=Boss(200,200)
    all_spritesBoss.add(theWife)
    player = cupHeadPlayer(all_spritesLevel1)
    player1=cupHeadPlayer(all_spritesLevel2)
    players=pygame.sprite.Group()
    bossGroup=pygame.sprite.Group()
    players.add(player)
    all_spritesLevel2.add(player1)
    all_spritesLevel2.add()
    back=backGround.get_rect()
    enemiesLevel2=pygame.sprite.Group()
    backStart=startScreenImage.get_rect()
    enemyShots=pygame.sprite.Group()
    bullets1=pygame.sprite.Group()
    bullets2=pygame.sprite.Group()
    bullets3=pygame.sprite.Group()
    enemies=pygame.sprite.Group()
    landsLevel1=pygame.sprite.Group()
    mainGround=Land(0,HEIGHT-4, 5000, 4)
    mainGround1=Land(0,HEIGHT-4, 5000, 4)
    mainGroundBoss=Land(0,HEIGHT-4,WIDTH,4)
    landsLevel1.add(mainGround)
    landsLevel2.add(mainGround1)
    landsLevel1.add(Land((WIDTH+90)/2,HEIGHT*3/5, 35, 50))
    landsLevel1.add(Land(WIDTH/2-50,HEIGHT*6/7,40,40))
    landsLevel1.add(Land(WIDTH+300,HEIGHT*9/10,50,50))
    landsLevel1.add(Land(WIDTH+200,HEIGHT*8/10,60,60))
    landsLevel1.add(Land(WIDTH+300,HEIGHT*7/10,60,47))
    landsLevel1.add(Land(WIDTH+400,HEIGHT*9/10,55,60))
    landsLevel1.add(Land(WIDTH+600,HEIGHT*7/10,32,60))
    landsLevel1.add(Land(WIDTH+500,HEIGHT*9/10,60,32))
    landsLevel1.add(Land(WIDTH+100,HEIGHT*7/10,29,60))
    landsLevel1.add(Land(WIDTH+300,HEIGHT*7/11,60,46))
    landsLevel1.add(Land((WIDTH+37)/2,HEIGHT*3/5, 35, 50))
    landsLevel1.add(Land(WIDTH/4-22,HEIGHT*6/7,40,40))
    landsLevel1.add(Land(WIDTH+102,HEIGHT*9/10,50,50))
    landsLevel1.add(Land(WIDTH+500,HEIGHT*8/10,60,60))
    landsLevel1.add(Land(WIDTH+600,HEIGHT*7/10,60,47))
    landsLevel1.add(Land(WIDTH+700,HEIGHT*9/10,55,60))
    landsLevel1.add(Land(WIDTH+497,HEIGHT*7/10,32,60))
    landsLevel1.add(Land(WIDTH+704,HEIGHT*9/10,60,32))
    landsLevel1.add(Land(WIDTH+451,HEIGHT*7/10,29,60))
    landsLevel1.add(Land(WIDTH+306,HEIGHT*7/11,60,46))
    landsLevel1.add(Land(WIDTH+111,HEIGHT*9/10,60,60))
    landsLevel2.add(Land((WIDTH+300)/2,HEIGHT*3/5, 35, 50))
    landsLevel2.add(Land(WIDTH/2-80,HEIGHT*4/7,40,40))
    landsLevel2.add(Land(WIDTH+600,HEIGHT*9/10,50,50))
    landsLevel2.add(Land(WIDTH+908,HEIGHT*8/10,60,60))
    landsLevel2.add(Land((WIDTH+150)/2,HEIGHT*4/5, 100, 50))
    landsLevel2.add(Land(WIDTH/2-100,HEIGHT*4/9,35,35))
    landsLevel2.add(Land(WIDTH+403,HEIGHT*9/12,50,35))
    landsLevel2.add(Land(WIDTH+1100,HEIGHT*8/10,65,60))
    landsLevel2.add(Land((WIDTH+980)/2,HEIGHT*3/5, 35, 50))
    landsLevel2.add(Land(WIDTH*3/10,HEIGHT*4/7,40,40))
    landsLevel2.add(Land(WIDTH+549,HEIGHT*9/10,50,50))
    landsLevel2.add(Land(WIDTH+867,HEIGHT*8/10,60,60))
    landsLevel2.add(Land((WIDTH+234)/2,HEIGHT*4/5, 100, 50))
    landsLevel2.add(Land(WIDTH/2-100,HEIGHT*4/9,35,35))
    landsLevel2.add(Land(WIDTH+407,HEIGHT*9/12,50,35))
    landsLevel2.add(Land(WIDTH+1000,HEIGHT*8/10,65,60))
    for j in range(1,6):
        landsLevel2.add(Land(WIDTH+40*j, HEIGHT-40*j, 50,50))
        landsLevel2.add(Land(WIDTH+300-40*j, HEIGHT-40*j,50,50))
    landsBoss.add(mainGroundBoss)
    bossPlayer=cupHeadPlayer(all_spritesBoss)
    all_spritesBoss.add(bossPlayer)
    overWorldSprites=pygame.sprite.Group()
    for i in range(1,7):
        enemies.add(Enemy())
    for x in enemies:
        all_spritesLevel1.add(x)
    for l in landsLevel1:
        all_spritesLevel1.add(l)
    all_spritesLevel1.add(player)
    for land in landsLevel2:
        all_spritesLevel2.add(land)
    for i in range(1,9):
        enemiesLevel2.add(Enemy())
    for x in enemiesLevel2:
        all_spritesLevel2.add(x)
    bossGroup.add(theWife)
    def draw_text(screen, string, fontSize, x,y, color, type):
        fontName=pygame.font.match_font(type)
        type = pygame.font.Font(fontName, fontSize)
        text_surface = type.render(string, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
    def playGameOver(playerScore):
        while(True):
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    overWorld=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        main()
            screen.fill(BLACK)
            draw_text(screen,"Game Over! You scored: "+str(playerScore),
             50,WIDTH/2,HEIGHT/2, WHITE,"Arial" )
            pygame.display.flip()
    overWorld=False
    introScreen=True
    running = True
    WispyWoods=Level(170,380,9,False,"Wispy Woods")
    DustyDunes=Level(500,280,9,False,"Dusty Dunes")
    FinalBoss=Level(273, 259,15,False,"The Widowed")
    overPlayer=OverWorldPlayer(WIDTH/7, 200)
    overWorldSprites.add(overPlayer)
    overWorldSprites.add(WispyWoods)
    overWorldSprites.add(DustyDunes)
    overWorldSprites.add(FinalBoss)
    woods,desert,boss=False,False,False
    def runOverWorld(xPoint,yPoint):
        woods,desert,boss=False,False,False
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    overWorld=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p and woods and not WispyWoods.beat:
                        overWorld=False
                        level1=True
                        running=True
                        return
                    elif event.key==pygame.K_p and desert\
                    and not DustyDunes.beat:
                        #print("HI")
                        overWorld=False
                        level2=True
                        running=True
                        return
                    elif event.key==pygame.K_p and boss:
                        overWorld=False
                        finalBoss=True
                        running=True
                        return
            overWorldSprites.update()
            screen.fill(BLACK)
            screen.blit(TheOverWorld,back)
            if pygame.sprite.collide_circle(overPlayer,WispyWoods):
                str="Play "+WispyWoods.getLevelName()+" ?"
                draw_text(screen, str, 29, 670, 25, WHITE, "Comic Sans")
                woods=True
            elif pygame.sprite.collide_circle(overPlayer, DustyDunes):

                str="Play "+DustyDunes.getLevelName()+" ?"
                draw_text(screen, str, 29, 670, 25, WHITE, "Comic Sans")
                desert=True
            elif pygame.sprite.collide_circle(overPlayer,FinalBoss):
                if WispyWoods.beat and DustyDunes.beat:
                    str="Play "+FinalBoss.getLevelName()+" ?"
                    draw_text(screen, str, 29, 670, 25, WHITE, "Comic Sans")
                    boss=True
                else:
                    str="You still have to beat other levels!"
                    draw_text(screen,str,18,670,25,WHITE,"Comic Sans")
            else:
                woods,desert,boss=False,False,False
            for elem in overWorldSprites:
                if isinstance(elem,Level):
                    attr=elem.getAttributes()
                    pygame.draw.circle(screen, attr[3],(attr[0],
                    attr[1]),attr[2],0)
            overWorldSprites.draw(screen)
            pygame.display.flip()
   #runs the explanation tutorial
    def runTutorial():
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        return
            screen.fill(BLACK)
            draw_text(screen,"Instructions:",42, WIDTH/2, HEIGHT*1/5, WHITE,
             "Comic Sans")
            draw_text(screen, "Move with Arrows!", 36, WIDTH/2, HEIGHT*2/5,
             WHITE,"Comic Sans" )       
            draw_text(screen,"Shoot with SpaceBar and Jump with S!",
             34, WIDTH/2, HEIGHT*3/5,WHITE,"Comic Sans")
            draw_text(screen, "Select Red Levels with P", 
            34,WIDTH/2,HEIGHT*4/5,WHITE,"Comic Sans")
            pygame.display.flip()
    #displays the win screen
    def runYouWin():
        introScreenFrame=0
        while True:
            clock.tick(FPS)
            introScreenFrame+=1
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        main()
            
            screen.fill(BLACK)
            screen.blit(startScreenImage,back)
            screen.blit(BLITRUNRIGHT[introScreenFrame%len(BLITRUNRIGHT)],
            ((WIDTH-50)/2, HEIGHT-70))
            draw_text(screen,"You win!",30,WIDTH/2,HEIGHT*2/5,WHITE,
            "Comic Sans")
            pygame.display.flip()
    
    #runs the intro
    def runIntro():
        introScreenFrame=0
        #global introScreen
        while True:
            clock.tick(FPS)
            introScreenFrame+=1
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        #global introScreen
                        return
                        #running=True
            screen.fill(BLACK)
            screen.blit(startScreenImage,back)
            screen.blit(BLITRUNRIGHT[introScreenFrame%len(BLITRUNRIGHT)],
            ((WIDTH-50)/2, HEIGHT-70))
            draw_text(screen,"CUPHEAD:The Devil's Wife",72, WIDTH/2,
             HEIGHT*2/5, BLACK, "Comic Sans")
            draw_text(screen, "Press P to start!", 20, WIDTH/2, 
            HEIGHT*3/5, BLACK,"Comic Sans" )
            pygame.display.flip()
    BossCount=0
    level1=False
    level2=False
    boss=False
    #the main game loop that shows the appropriate sprites and such
    while running:
        clock.tick(FPS)
        if introScreen:
            runIntro()
            introScreen=False
            tutorial=True
            #overWorld=True
            # overWorld=True
        if tutorial:
            runTutorial()
            tutorial=False
            overWorld=True
        if  overWorld:
            print(WispyWoods.beat)
            runOverWorld(200,200)
            overWorld=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    introScreen=True
                if event.key == pygame.K_SPACE :
                    if not WispyWoods.beat:
                        player.shoot()
                    elif WispyWoods.beat and not DustyDunes.beat:
                        player1.shoot()
                    elif WispyWoods.beat and DustyDunes.beat\
                    and not FinalBoss.beat:
                        bossPlayer.shoot()
                if event.key == pygame.K_s:
                    if not WispyWoods.beat:
                        player.jump()
                    elif WispyWoods.beat and not DustyDunes.beat:
                        player1.jump()
                    elif WispyWoods.beat and DustyDunes.beat\
                    and not FinalBoss.beat:
                        bossPlayer.jump()
                if event.key==pygame.K_TAB:
                    if not WispyWoods.beat:
                        player.gun=(player.gun+1)%len(BulletTypes)
                    elif WispyWoods.beat and not DustyDunes.beat:
                        player1.gun=(player1.gun+1)%len(BulletTypes)
                    elif WispyWoods.beat and DustyDunes.beat\
                    and not FinalBoss.beat:
                        bossPlayer.gun=(bossPlayer.gun+1)%len(BulletTypes)
                if event.key==pygame.K_p and WispyWoods.beat and DustyDunes.beat:
                    overWorld=False
        #booleans to check which level we are in and what to show to player
        if not WispyWoods.beat:
            all_spritesLevel1.update()
        elif not DustyDunes.beat and WispyWoods.beat: 
            all_spritesLevel2.update()
        elif not FinalBoss.beat and DustyDunes.beat and WispyWoods.beat:
            all_spritesBoss.update()
        #collision checker for enemies and bullets
        deaths=pygame.sprite.groupcollide(enemies, bullets1, True, True)
        deaths1=pygame.sprite.groupcollide(enemies, bullets2, True, True)
        deaths2=pygame.sprite.groupcollide(enemies, bullets3, True, True)
        deaths3=pygame.sprite.groupcollide(enemiesLevel2,bullets1,True,True)
        deaths4=pygame.sprite.groupcollide(enemiesLevel2,bullets2,True,True)
        deaths5=pygame.sprite.groupcollide(enemiesLevel2,bullets3,True,True)
        playerScore+=100*len(deaths)
        playerScore+=100*len(deaths1)
        playerScore+=100*len(deaths2)
        #jumping concept taken from same place
        # https://www.youtube.com/watch?v=_y5U8tB36Vk
        if player.velocity.y>0 and not WispyWoods.beat:
            ontop=pygame.sprite.spritecollide(player, landsLevel1, False)
            if ontop : 
                player.position.y=ontop[0].rect.top+1
                player.velocity.y=0
        elif WispyWoods.beat and player1.velocity.y>0 and not DustyDunes.beat:
            ontop=pygame.sprite.spritecollide(player1, landsLevel2, False)
            if ontop : 
                player1.position.y=ontop[0].rect.top+1
                player1.velocity.y=0
        elif WispyWoods.beat and DustyDunes.beat and\
         bossPlayer.velocity.y>0 and not FinalBoss.beat:
            ontop=pygame.sprite.spritecollide(bossPlayer,landsBoss, False)
            if ontop : 
                bossPlayer.position.y=ontop[0].rect.top+1
                bossPlayer.velocity.y=0
    
        if not WispyWoods.beat and player.rect.right >= WIDTH*3/4:
            for land in landsLevel1:
                land.rect.x-=player.velocity.x
            
            player.position.x-=player.velocity.x
            
        elif not WispyWoods.beat and player.rect.right <= WIDTH/4:
            if player.distanceFromBeginning>95:
                for land in landsLevel1:
                    land.rect.x+=abs(player.velocity.x)
                player.position.x+=player.velocity.x
        if WispyWoods.beat and not DustyDunes.beat and player1.rect.right >= WIDTH*3/4:
            for land in landsLevel2:
                land.rect.x-=player1.velocity.x
            player1.position.x-=player1.velocity.x
        elif WispyWoods.beat and not DustyDunes.beat and player1.rect.right<=WIDTH/4:
            if player1.distanceFromBeginning>95:
                for land in landsLevel2:
                    land.rect.x+=abs(player1.velocity.x)
                player1.position.x+=player1.velocity.x
        bossHealth-=1.2*len(pygame.sprite.groupcollide(bullets1, bossGroup, True, False))
        bossHealth-=len(pygame.sprite.groupcollide(bullets2, bossGroup, True, False))
        bossHealth-=3.1*len(pygame.sprite.groupcollide(bullets3, bossGroup, True, False))
        #change back to 3000
        if player.distanceFromBeginning>=2700:
            player.distanceFromBeginning=0
            WispyWoods.beat=True
            overWorld=True
        if player1.distanceFromBeginning>=2700:
            player1.distanceFromBeginning=0
            DustyDunes.beat=True
            overWorld=True
        if bossHealth<=0:
            theWife.kill()
            if BossCount==0:
                playerScore+=50*100
                BossCount+=1
            runYouWin()
        #keeps track of cupheads health
        cupHeadHealth-=len(pygame.sprite.groupcollide(players, enemies, False, False, pygame.sprite.collide_circle))
        cupHeadHealth-=len(pygame.sprite.groupcollide(players, enemyShots, False, True, pygame.sprite.collide_circle))
        if cupHeadHealth<=0:
            player.kill()
            dead=True
            if dead:
                playGameOver(playerScore)
        #picks which screen to blit to the view
        if not WispyWoods.beat:
            screen.fill(BLACK)
            screen.blit(startScreenImage, back)
            all_spritesLevel1.draw(screen)
            draw_text(screen, str(playerScore), 50, WIDTH-90, 70,WHITE, "Times" )
            draw_text(screen,"Health: "+str(cupHeadHealth), 25,WIDTH-60,60,WHITE,"Comic Sans")
            pygame.display.flip()
        elif not DustyDunes.beat and not overWorld:
            screen.fill(BLACK)
            DuneBackground=pygame.transform.scale(DuneBackground,(WIDTH,HEIGHT))
            screen.blit(DuneBackground, back)
            all_spritesLevel2.draw(screen)
            draw_text(screen,"Health: "+str(cupHeadHealth), 25,WIDTH-60,60,WHITE,"Comic Sans")
            pygame.display.flip()
        elif DustyDunes.beat and WispyWoods.beat and not overWorld:
            overWorld=False
            print("hi")
            screen.fill(BLACK)
            lair=pygame.transform.scale(lair,(WIDTH,HEIGHT))
            screen.blit(lair,back)
            all_spritesBoss.draw(screen)
            draw_text(screen,"Health: "+str(cupHeadHealth), 25,WIDTH-60,60,WHITE,"Comic Sans")
            pygame.display.flip()
main()