import pygame
import random
pygame.init()
class Spirt(pygame.sprite.Sprite):
    def __init__(self, filename, width, height, x, y):
        self.filename = filename
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(self.filename), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(Spirt):
    def __init__(self, filename, width, height, x, y, speed):
        super().__init__(filename, width, height, x, y)
        self.speed = speed
    def wasd(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 410:
            self.rect.y += self.speed
    def wasd_1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed
class ball(Player):
    def __init__(self, filename, width, height, x, y, speed, speed_1):
        super().__init__(filename, width, height, x, y, speed)
        self.speed_1 = speed_1
    def wasd_2(self):
        if flag_start:
            a = random.randint(0, 1)
            if a == 0:
                self.speed *= 1
                self.speed_1 *= -1
                #self.rect.y += self.speed
            elif a == 1:
                #self.rect.x -= self.speed
                self.speed *= -1
                self.speed_1*=1
        else:
            if self.rect.x <= 0 and self.rect.y <= 0:
                self.speed *= -1
                self.speed_1 *= -1
            if self.rect.x >= 700 and self.rect.y >= 410:
                self.speed *= -1
                self.speed_1 *= -1
            if self.rect.x <= 0 and self.rect.y >= 410:
                self.speed *= -1
                self.speed_1 *= -1
            if self.rect.x >= 700 and self.rect.y <= 0:
                self.speed *= -1
                self.speed_1 *= -1
            if (self.rect.x <= 0 and ((self.rect.y <= 0) == False)) or (self.rect.x >= 700 and ((self.rect.y >= 410)==False)):
                self.speed *= -1
                self.speed_1 *= 1
            
            if (((self.rect.x <= 0)==False) and self.rect.y >= 410) or (((self.rect.x >= 700) == False) and self.rect.y <= 0):
                self.speed *= 1
                self.speed_1 *= -1
            
        self.rect.x += self.speed
        self.rect.y += self.speed_1

back = Spirt("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/p_back.png", 750, 500, 0, 0)
player = Player("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/gamer_1.png", 25, 88, 35, 150, 5)
player_1 = Player("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/gamer_2.png", 25, 88, 680, 150, 5)
balli = ball("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/ball.png", 60, 60, 250, 300, 10, 10)
clock = pygame.time.Clock()
game = True
flag_start = True
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Ping: 9999")
i = 0
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    back.reset()
    balli.reset()
    if i <= 0:
        flag_start = False
    

    balli.wasd_2()
    
    player.reset()
    player.wasd()
    player_1.reset()
    player_1.wasd_1()
    i = 10
    pygame.display.update()
    clock.tick(60)