from pygame import *
#Классы
class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
 
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < 1700:
            self.rect.x += self.speed


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
