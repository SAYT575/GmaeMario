import play
import pygame
from random import randint

pygame.mixer_music.load('soundtrack.mp3')
pygame.mixer_music.play()

#play.set_backdrop('light green')
fone = play.new_image(image="fone.png",x=0,y=50)
player = play.new_image(image="1.jpg",x=-240,y=235,size=20)


#тут подключи нужны звуки. Например, звук сбора монетки
#счетчик монет
score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.top-30, size=70)
score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.top-30, size=70)
#подсказки
text = play.new_text(words='Tap SPACE to jump, LEFT/RIGHT to move', x=0, y=play.screen.bottom+60, size=70)

sea = play.new_box(
        color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    )

def draw_platforms():
    #добавь сюда платформы, по которым будет перемещаться персонаж
    platform = play.new_image(image="3.png",x=-240, y=150,size= 60)
    platform2 = play.new_image(image="3.png",x=25, y= 190,size= 60)
    platform3 = play.new_image(image="3.png",x=290, y= 150,size= 60)
    platform4 = play.new_image(image="3.png",x=220, y=50,size= 60)
    platform5 = play.new_image(image="3.png",x=-10, y=30,size= 60)
    platform6 = play.new_image(image="3.png",x=-240,y=40,size= 60)
    platform.start_physics(can_move=False)
    platform2.start_physics(can_move=False)
    platform2.start_physics(can_move=False)
    platform3.start_physics(can_move=False)
    platform4.start_physics(can_move=False)
    platform5.start_physics(can_move=False)
    platform6.start_physics(can_move=False)
    player.start_physics(can_move=True)
    
coints=[]
def draw_coins():
    #добавь сюда монетки, которе будет собирать персонаж
    coint1 = play.new_image(image="qqq.png",x=25, y= 237,size=4)
    coints.append(coint1)
    coint2 = play.new_image(image="qqq.png",x=290, y=195,size=4)
    coints.append(coint2)
    coint3 = play.new_image(image="qqq.png",x=220, y= 95,size=4)
    coints.append(coint3)
            #coint4 = play.new_circle(color="yellow",radius=30,x=-5, y=70)
            #coints.append(coint4)
    coint5 = play.new_image(image="qqq.png",x=-5, y=75,size=4)
    coints.append(coint5)
    coint6 = play.new_image(image="qqq.png",x=-240, y=87,size=4)
    coints.append(coint6)

    
@play.when_program_starts
def start():
    #подключи 
    player.start_physics(can_move = True, stable=True,obeys_gravity=True, bounciness=1, mass=1,friction=20)
    draw_platforms()
    draw_coins()

@play.repeat_forever
async def game():
    #тут опиши процесс игры
    for c in coints:
        if c.is_touching(player):
            score.words=str(int(score.words)+1)

    for c in coints:
        if c.is_touching(player):
            c.hide()
            coints.remove(c)
    if play.key_is_pressed('a'):
        player.physics.x_speed = -10
    elif play.key_is_pressed("d"):
        player.physics.x_speed = 10
    elif play.key_is_pressed("space"):
        player.physics.y_speed = 0
        await play.timer(seconds = 1)
        player.physics.y_speed = 0
    else:
        player.physics.x_speed = 0
    if player.is_touching(sea):
        await play.timer(seconds=1/48)
        player.hide()
        quit()
    

play.start_program()