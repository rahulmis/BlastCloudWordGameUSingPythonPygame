def new_word():
    global word_x,word_y,text,chosen_word,press_word,speed
    word_x = random.randint(100,600)
    word_y = 0
    chosen_word = random.choice(llist)
    press_word = ''
    speed += 0.02
    text = font.render(chosen_word,True,black)
import pygame
import sys
import random
import time
pygame.init()
################################# colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
################################## variables
x = 900
y = 600
speed = 0.5
point = 0
llist = ['apple','mango','banana','yellow','green','man','girl','boy']
font = pygame.font.SysFont('ComicSansMs',45)
text1 = font.render('Hit Enter To Restart The Game...', True, red)
################################# screen
win = pygame.display.set_mode((x,y))
pygame.display.set_caption('Blast Cloud Word Game')
################################ images
logo = pygame.image.load('jj.png')
background1 = pygame.image.load('1.png')
background2 = pygame.image.load('2.png')
cloud = pygame.image.load('clipart984165.png')
matchimg = pygame.image.load('explosion1.gif')
pygame.display.set_icon(logo)
##################################### sounds
pygame.mixer.music.load('bgmuisc.wav')
channel0 = pygame.mixer.Channel(0)
channel0.set_volume(0.3)
channel1 = pygame.mixer.Channel(1)
channel1.set_volume(0.3)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
blastmusic = pygame.mixer.Sound('boom.wav')
lostmusic = pygame.mixer.Sound('loss1.wav')
#####################################
new_word()
############################################ infinite game loop
while True:
    if(point >= 100):
        win.blit(background2, (0, 0))
    else:
        win.blit(background1,(0,0))
    win.blit(cloud,(word_x-40,word_y-20))
    win.blit(text,(word_x,word_y))
    word_y += speed
    word_caption = font.render(chosen_word,True,red)
    win.blit(word_caption,(10,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif(event.type == pygame.KEYDOWN):
            press_word += pygame.key.name(event.key)
            if chosen_word.startswith(press_word):
                text = font.render(press_word,True,blue)
                if(chosen_word == press_word):
                    point += len(chosen_word)
                    channel0.play(blastmusic,maxtime=600)
                    win.blit(matchimg,(word_x,word_y))
                    pygame.display.update()
                    time.sleep(0.02)
                    new_word()
            else:
                text = font.render(press_word,True,red)
                press_word = ''
    point_caption = font.render(str(point),True,blue)
    win.blit(point_caption,(10,5))
    if(word_y < y-5):
        pass
    else:
        bb = pygame.mixer.Channel(1).get_busy()
        if bb == 1:
            pass
        else:
            channel1.play(lostmusic,maxtime=6000)
        win.blit(text1,(100,260))
        pygame.display.update()
        event = pygame.event.wait()
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            point = 0
            speed = 0.5
            new_word()
    pygame.display.update()