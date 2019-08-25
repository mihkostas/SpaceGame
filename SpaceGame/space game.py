import pygame
import random
h = 500
w = 700

black = (0,0,0)
score = 0
timer = 0

# X and y speed
xs = 0
ys = 3
ybs = 0
eys = 3
exs = 3
bossYs = 0
bossXs = 0
bbossYs = 0
bbossXs = 0
lifes = 3

#pygame constructor
pygame.init()
# load music and images
dis = pygame.display.set_mode([w,h])
s = pygame.mixer.Sound("8-Bit-Mayhem.ogg")
s.play(-1)
s2 = pygame.mixer.Sound("Battle-Unison_intro.ogg")
s3 = pygame.mixer.Sound("Battle-Unison_loop.ogg")
pygame.display.set_caption("space game")
img = pygame.image.load("bg.png")
imgs = pygame.image.load("sps.png")
bimg = pygame.image.load("b1.png")
bimg2 = pygame.image.load("b1.png")
eimg = pygame.image.load("enemy.png")
BossImg = pygame.image.load("boss.png")
c = pygame.time.Clock()

    

#Flags
fl = True
flag69 = 1
bossfl = 1  

# Y and X of objects
y = 10
x = 10
y2 = y-500
x2 = x
y3 = 400
x3 = 310
yb = 0
xb = -30
ey = 20
ex = 200
bossY = -135
bossX = 300
bbossY = 0
bbossX = -30

ran = 0
ran2 = 0
#font for the texts on the screen
font = pygame.font.SysFont("monospace", 17)
font2 = pygame.font.SysFont("monospace", 70)
txt = ""

#display images on the screen functions
def boss(x,y):
    dis.blit(BossImg,(x,y))
    
def enemy(x,y):
    dis.blit(eimg,(x,y))
    
def bullet(x,y):
    dis.blit(bimg,(x,y))

def bullet2(x,y):
    dis.blit(bimg2,(x,y))
    
def sps(x,y):   
    dis.blit(imgs,(x,y)) 
def bg(x,y):
    dis.blit(img,(x,y))      
def bg2(x,y):
    dis.blit(img,(x,y))

#hitbox of ship to bullets 
def hitbox(Y,y,X,x):
    if Y <= y+8 and Y >= y:    
        if X <= x+44 and X >= x:
             return True


# main game loop            
while fl == True:
   #display score and lives
   ltext = font2.render(txt, True, (255,0,0))  
   text2 = font.render("lives "+str(lifes), True, (102,205,170))
   text = font.render("score "+str(score), True, (102,205,170))
   for ev in pygame.event.get():
       if ev.type == pygame.QUIT:
          fl = False
       #shoot bullets   
       if ev.type == pygame.KEYDOWN:
          if yb < 10: 
           if ev.key == pygame.K_SPACE:
                 pygame.mixer.music.load("bullet.mp3")
                 pygame.mixer.music.play(0)
                 xb = x3+7
                 yb = y3
                 ybs = -6
                 flag69 = 1
                 txt = ""
           
   #ship controls      
   keys = pygame.key.get_pressed()  
   if keys[pygame.K_a]:
             x3 += -5
   if keys[pygame.K_d]:
             x3 += 5

   #wall stop 
   if x3 >= w-50:
       x3-=5
   if x3 <=1:
       x3+=5
       
   # bg reset           
   if y>500:
       y =10-500
   if y2>500:
       y2 =10-500
   
   if score == 50:
       bossfl = 2
   #boss reset    
   if score == 150:
       bossfl = 1
       bossY = -135
       bossX = 300
       bossYs = 0
       bossXs = 0
       bbossYs = 0
       bbossXs = 0
       bbossY = 0
       bbossX = -30
       if timer != 0:
        s.stop()
        s3.stop()
        s.play(-1)
       timer = 0
       
       
       
   if bossfl == 1:
     bimg = pygame.image.load("b1.png")
     if  yb <=  ey+10 and yb >= ey:
       if xb <= ex+58 and xb >= ex-12 :
           pygame.mixer.music.load("expl.mp3")
           pygame.mixer.music.play(0)
           ey = -350
           ex =  random.randint(1,w)
           ran = random.randint(1,2)
           ran2 = random.randint(1,4)
           score+=1

  
           
     if flag69 ==1:
         
        if x3 <= ex+70 and x3 >= ex:
              if  y3 <=  ey+4.5 and y3 >= ey:
     
                  lifes-=1




        if ey >= 50 and  ey <= 55:
               bbossY = ey
               bbossX =  ex
           
               bbossYs = 10


         
     if ey > h:
        ey = -40
        ex =  random.randint(1,w)
        ran = random.randint(1,2)
        ran2 = random.randint(1,4)
     if ran == 1:
       eys = 4
       exs = 2
     if ran == 2:
       eys = 4
       exs = -2
     if ran2 == 2:
       eimg = pygame.image.load("enemy2.png")
       exs = 0
       eys = 5
     else:
       eimg = pygame.image.load("enemy.png")

   #lifes  
   if lifes <=0:
       txt = "You lose"
       bossY = -135
       bossX = 300
       bossYs = 0
       bossXs = 0
       bbossYs = 0
       bbossXs = 0
       bbossY = 0
       bbossX = -30
       timer = 0
       s3.stop()
       flag69 = 2
       bossfl = 1
       score = 0
       lifes = 3
       s.stop()
       s.play(-1)
       




   bossY+=bossYs
   bossX+=bossXs
   bbossY+=bbossYs
   bbossX+=bbossXs
   ey+=eys
   ex+=exs
   
   yb+=ybs    
   y+=ys
 
   y2+=ys
   dis.fill(black)
   
   bg(x,y)  
   bg2(x2,y2)
   #boss       
   if bossfl == 2:
       bimg = pygame.image.load("b2.png") 
       if timer == 0: 
          bbossYs = 0
          bbossY = -200
       s.stop()
       if  yb <=  bossY+20 and yb >= bossY:
        if xb <= bossX+70 and xb >= bossX-12:
            score+=1

       
       timer+=1
       boss(bossX,bossY)
           
       if timer < 700 and timer > 500 :
          bossYs = 1
          
       if timer == 1:
           s2.play()
          
       if timer == 700:
           bossYs = 0
           bossXs = 5  
           bbossY = bossY+100
           bbossX = bossX+50
           bbossYs = 10
           
       if bbossY > h:
           bbossY = bossY+100
           bbossX = bossX+50
       
       if bossX > 600:

             bossXs = -5
       if bossX < 1:
             bossXs = 5
             
       if timer == 1262:
          s3.play(-1)
          
       if timer >= 3000:
           if bossX > 600:
             bossXs = -7
           if bossX < 1:
             bossXs = 7
       if timer >= 6000:
           if bossX > 600:
             bossXs = -9
           if bossX < 1:
             bossXs = 9
             
       if timer >= 9000:
           if bossX > 600:
             bossXs = -12
           if bossX < 1:
             bossXs = 12
           
    
       
   if flag69==1:
     enemy(ex,ey)
     
   
   if hitbox(bbossY,y3,bbossX,x3) == True:
             lifes-=1
  
   bullet2(xb,yb)
   bullet(bbossX,bbossY)
   sps(x3,y3)
   dis.blit(text,
   (10,10))
   dis.blit(text2,
   (10,40))
   dis.blit(ltext,
   (200 - text.get_width() // 2, 170 - text.get_height() // 2))
   pygame.display.update()
   c.tick(60)
   

pygame.quit()
quit()
