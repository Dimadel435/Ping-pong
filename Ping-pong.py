from pygame import *

#Сцена
back = (200,255,255)
window = display.set_mode((600,500))
window.fill(back)

#fps
clock = time.Clock()
FPS = 60

#Цикл
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        display.update()
        clock.tick(FPS)