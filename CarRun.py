
import random
import time
import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('car run')
background = pygame.image.load('abcd4.png')
lower = pygame.image.load('lower.png')
player = pygame.image.load('car.png  ')
red = (255,0,0)
bright_green = (142,214,127)
white = (120,24,40)
titleColor = (0,0,255)
def GameExit():
    pygame.quit()
    quit()
imgx = -40
imgy =570
j = 0
score = 0
speed = 0.05
score = 0
play ='Level1'
def rawat():
    font = pygame.font.SysFont("comicsansms",10)
    text = font.render('@rawat',True,titleColor)
    gameDisplay.blit(text,(5,580))

    
def GameLoop():
   player_y = 470
   player_x = 20
   blockX = 800
   blockY = 0
   crashedVar = 520
   crashedVar1 = 20 
   global imgx,imgy,j,speed,score,choice,pause
   pause = True
   font = pygame.font.SysFont("comicsansms",35)
   if play == 'Level1':
       file = open('score.exe','r')
   else: 
       file = open('score1.exe','r')
   higestScore = file.read()
   file.close()
   if play == 'Level2':
       obstrical = pygame.image.load('carr3.png')
       background = pygame.image.load('back2.jpg')
       blockY = 535
   else:
       obstrical = pygame.image.load('piperun0.png')
       background = pygame.image.load('bkg1.png')
       blockY = 465

        
   global score
   score = 0
   while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
                if event.key == pygame.K_SPACE:
                    for i in range(0,8):
                        player_y-=50
                        gameDisplay.blit(background,(j,0))
                        gameDisplay.blit(player,(20,player_y))
                        gameDisplay.blit(obstrical,(blockX,blockY))#465
                        gameDisplay.blit(lower,(imgx,imgy))
                        j-=5
                        if j<-500:
                            j = 0

                        time.sleep(0.05)
                        blockX-=10
                        if blockX < -25:
                            blockX = random.randrange(600,800)
                            score+=1
                        imgx-=10
                        if imgx<-50:
                            imgx = 0
                        text = font.render("Higest Score "+higestScore,True,red)
                        gameDisplay.blit(text,(500,50))
                        text = font.render("Score "+str(score),True,red)
                        gameDisplay.blit(text,(50,50))
                        pygame.display.update()
                    for i in range(0,8):
                        gameDisplay.blit(background,(j,0))
                        gameDisplay.blit(obstrical,(blockX,blockY))
                        gameDisplay.blit(player,(20,player_y))
                        gameDisplay.blit(lower,(imgx,imgy))
                        player_y+=50
                        if play == 'Level1':                            
                            crashedVar = 490
                            crashedVar1 = 63 

                        if blockX < 100 and player_y >=crashedVar:  #blockX < 75 and player_y >=520
                            gameDisplay.blit(background,(j,0))
                            gameDisplay.blit(obstrical,(blockX,blockY))
                            gameDisplay.blit(player,(20,player_y-crashedVar1))#-20
                            gameDisplay.blit(lower,(imgx,imgy))
                            pygame.display.update()
                            time.sleep(1)
                            scoreHigest(score)
                            crashed()
                        time.sleep(0.05)
                        blockX-=10
                        j-=5
                        if j<-500:
                            j = 0
                        if blockX < -25:
                            
                            score+=1
                            blockX = random.randrange(600,800)
                            if score == 5:
                                speed = 0.04
                            elif score == 8:
                                speed = 0.03
                            elif score == 11:
                                speed = 0.02
                            elif score == 14:
                                speed = 0.001
                                
                            if play == 'Level2':
                                pipe = ['carr3.png','carr4.png','carr5.png','carr2.png']
                            else:
                                pipe = ['piperun.png','piperun0.png']#,'piperun1.png','piperun2.png','piperun3.png','piperun4.png','piperun5.png']
                                
                            choice = random.choice(pipe)
                            obstrical = pygame.image.load(choice)
                        imgx-=10
                        if imgx<-50:
                            imgx = 0
                        text = font.render("Higest Score "+higestScore,True,red)
                        gameDisplay.blit(text,(500,50))
                        text = font.render("Score "+str(score),True,red)
                        gameDisplay.blit(text,(50,50))
                        pygame.display.update()
            
            imgx+=10
        gameDisplay.blit(background,(j,0))
        gameDisplay.blit(player,(player_x,player_y))
        gameDisplay.blit(obstrical,(blockX,blockY))

        gameDisplay.blit(lower,(imgx,imgy))
        rawat()
        text = font.render("Higest Score "+higestScore,True,red)
        gameDisplay.blit(text,(500,50))
        text = font.render("Score "+str(score),True,red)
        gameDisplay.blit(text,(50,50))

        if blockX < 98 and player_y >=490:
            time.sleep(1)
            scoreHigest(score)
            crashed()
        j-=5
        if j<-500:
            j = 0

        blockX-=10
        if blockX < -40 :
            
            blockX = random.randrange(600,800)
        time.sleep(speed)

        imgx-=10
        if imgx<-50:
            imgx = 0
        player_y = 545 #515
        pygame.display.update()
def scoreHigest(score):
    global play
    if play == 'Level1':
        file = open('score.exe','r')
    else:
        file = open('score1.exe','r')
    higestScore = (file.read())
    file.close()
    if score > int(higestScore):
        if play == 'Level1':
            file = open('score.exe','w')
        else:
            file = open('score1.exe','w')
        file.write((str(score)))
        ##print('score',score)
        file.close()

def crashed():
    j = 0
    imgx = -40
    imgy = 570
    x= 350
    car = 'car2.png' 
    player = pygame.image.load(car)
    global score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit()
        if play == 'Level2':
           background = pygame.image.load('back2.jpg')
        else:
           background = pygame.image.load('bkg1.png')
        gameDisplay.blit(background,(j,0))
        gameDisplay.blit(lower,(imgx,imgy))
        gameDisplay.blit(player,(x,540))
        time.sleep(0.10)
        font = pygame.font.SysFont("comicsansms",90)
        text = font.render('CRASHED',True,titleColor)
        gameDisplay.blit(text,(220,0))
        font = pygame.font.SysFont("comicsansms",60)
        text = font.render('YOU SCORE  '+str(score),True,titleColor)
        gameDisplay.blit(text,(220,130))
        rawat()
        button('RESTART!',340,250,170,30,white,bright_green,GameLoop)
        button('MENU!',350,325,110,30,white,bright_green,gameIntro)
        button('QUIT!',350,400,110,30,white,bright_green,GameExit)
        imgx-=10
        if imgx<-50:
            imgx = 0
        j-=5
        if j<-500:
            j = 0
        x+=20
        if x > 800:
            x = -40
            car = ['car1.png','car2.png','car.png']
            choice = random.choice(car)
            player = pygame.image.load(choice)
        pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action = None):            ## BUTTON FUNCTION 
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    ###print(click)
    font = pygame.font.SysFont("comicsansms",35)
    
    if x+w >mouse[0]>x and y+h > mouse[1] >y:
        text = font.render(msg,True,ic)
        gameDisplay.blit(text,(x,y-10))
        if click[0]==1 and action != None:
             action()
    else:
        text = font.render(msg,True,ac)
        gameDisplay.blit(text,(x,y-10))
        
pause = True
def unpaused():             ## UNPAUSED FUNCTION MEANS CONTINUE THE PAUSED GAME
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
    
def paused():               ## PAUSED FUNCTION TO PAUSE THE GAME
    global pause
    pygame.mixer.music.pause()
    font = pygame.font.SysFont("comicsansms",90)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit()
        text = font.render('PAUSED',True,titleColor)
        gameDisplay.blit(text,(250,100))
        rawat()
        button('RESUME!',340,250,170,30,white,bright_green,unpaused)
        button('MENU!',350,325,110,30,white,bright_green,gameIntro)
        button('QUIT!',350,400,110,30,white,bright_green,GameExit)
        pygame.display.update()
    pause = True
def gameIntro():
    pygame.mixer.music.unpause()
    j = 0
    imgx = -40
    imgy = 570
    x= 350
    car = 'car2.png' 
    player = pygame.image.load(car)
    font = pygame.font.SysFont("comicsansms",90)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit()
        gameDisplay.blit(background,(0,0))
        gameDisplay.blit(player,(x,540))
        gameDisplay.blit(lower,(imgx,imgy))
        rawat()
        time.sleep(0.10)
        text = font.render('CAR RUN',True,titleColor)
        gameDisplay.blit(text,(230,50))
        button('START!',350,225,130,30,white,bright_green,GameLoop)
        button('LEVEL!',350,300,110,30,white,bright_green,levelFunction)
        button('QUIT!',350,375,110,30,white,bright_green,GameExit)
        j-=5
        if j<-500:
            j = 0
        imgx-=10
        if imgx<-50:
            imgx = 0
        x+=20
        if x > 800:
            x = -40
            car = ['car1.png','car2.png','car.png','car1.png','car2.png','car.png']
            choice = random.choice(car)
            player = pygame.image.load(choice)
        pygame.display.update()

def background_crash():
    pygame.mixer.music.load('CHALLENGE.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

def levelFunction():
    j = 0
    imgx = -40
    imgy = 570
    x= 350
    car = 'car2.png' 
    player = pygame.image.load(car)
    font = pygame.font.SysFont("comicsansms",90)
    levels = 0
    global play

    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        gameDisplay.blit(background,(0,0))
        if levels == 0:
            text = font.render('level 1',True,white)
            gameDisplay.blit(text,(300,200))
        else:
            text = font.render('level 2',True,white)
            gameDisplay.blit(text,(300,200))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    levels = 1
                if event.key == pygame.K_BACKSPACE:
                    levels = 0

        gameDisplay.blit(player,(x,540))
        gameDisplay.blit(lower,(imgx,imgy))
        rawat()
        time.sleep(0.10)
        if levels == 0:
            play = 'Level1'
        else:
             play = 'Level2'
        button('START!',500,400,130,30,white,bright_green,GameLoop)
        imgx-=10
        if imgx<-50:
            imgx = 0
        x+=20
        if x > 800:
            x = -40
            car = ['car1.png','car2.png','car.png']
            choice = random.choice(car)
            player = pygame.image.load(choice)
        pygame.display.update()
background_crash()
gameIntro()

