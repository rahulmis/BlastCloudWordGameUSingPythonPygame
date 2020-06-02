def new_word():
    global chossen_word,text,font,word_x,word_y,press_word,speed
    word_x = random.randint(100,600)
    word_y = 0
    press_word = ''
    speed += 0.05
    chossen_word = random.choice(lines)
    text = font.render(chossen_word,True,red)

import random
import pygame
import sys
import time
pygame.init()
######################################################## Variables used
x = 900
y = 600
speed = 0.5
point = 0
lines = ['hello','cow','fact','man', 'cloud', 'down', 'earth', 'google', 'facebook', 'what', 'is', 'there', 'animal', 'rose', 'rat', 'puppy', 'long', 'small', 'kite', 'young', 'loud', 'lord', 'fan', 'tv', 'film', 'flower', 'grapes', 'apple', 'onion', 'mango', 'banana', 'orange', 'queen', 'hen', 'horse', 'donkey', 'parrot','turn','toe','thumb']

######################################################## initalize screen and set title
win = pygame.display.set_mode((x,y))
pygame.display.set_caption('Cloud Blast Word Game')
#########################################################   Images
logo = pygame.image.load('jj.png')
background1 = pygame.image.load('1.png')
background2 = pygame.image.load('2.png')
cloud = pygame.image.load('clipart984165.png')
matchedimg = pygame.image.load('explosion1.gif')
########################################################## Add logo
pygame.display.set_icon(logo)
######################################################### Font
font = pygame.font.SysFont('ComicSansMs',45)
######################################################## Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
########################################################
text1 = font.render('Hit Enter To Restart The Game..', True, red)

######################################################## sounds
channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel1.set_volume(0.3)
pygame.mixer.music.load('bgmuisc.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
######################################################## call the new_word
new_word()
# run the game loop
while True:
    if point >=100:
        win.blit(background1, (0, 0))
    else:
        win.blit(background2,(0,0))
    win.blit(cloud,(word_x-40,word_y-20))
    win.blit(text,(word_x,word_y))
    word_y += speed
    wordCaption = font.render(chossen_word,True,red)
    win.blit(wordCaption,(10,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif(event.type == pygame.KEYDOWN):
            press_word += pygame.key.name(event.key)
            if chossen_word.startswith(press_word):
                text = font.render(press_word,True,blue)
                if(chossen_word == press_word):
                    point += len(chossen_word)
                    channel1.play(pygame.mixer.Sound('boom.wav'), maxtime=600)
                    win.blit(matchedimg, (word_x - 40, word_y - 20))
                    pygame.display.update()
                    time.sleep(0.02)
                    new_word()
            else:
                text = font.render(press_word, True, red)
                press_word = ''
    pointCaption = font.render(str(point),True,blue)
    win.blit(pointCaption,(10,5))
    if(word_y < y-5):
        pass
    else:
        bb = pygame.mixer.Channel(0).get_busy()
        if bb == 1:
            pass
        else:
            channel0.set_volume(0.8)
            channel0.play(pygame.mixer.Sound('loss1.wav'), maxtime=6000)
        win.blit(text1, (100,260))
        pygame.display.update()
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            channel0.stop()
            speed = 0.5
            point = 0
            new_word()
    pygame.display.update()
