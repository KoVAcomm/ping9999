import pygame
import random
pygame.init()
pygame.font.init()
sch_1 = 0
sch_2 = 0
class Spirt(pygame.sprite.Sprite):
    def __init__(self, filename, width, height, x, y):
        self.filename = filename
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(self.filename), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.top = self.rect.top
        self.botton = self.rect.bottom
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
        global sch_1
        global sch_2
        if flag_start:
            a = random.randint(0, 1)
            if a == 0:
                self.speed *= 1
                self.speed_1 *= -1
                
            elif a == 1:
                
                self.speed *= -1
                self.speed_1*=1
        else:
            
            if self.rect.y >= 450 or self.rect.y <= 0:
                self.speed *= 1
                self.speed_1 *= -1
            if self.rect.x <= 0 or self.rect.x >= 700:

                self.speed *= -1
                self.speed_1 *= 1
                if self.rect.x <= 0:
                    sch_2 +=1
                elif self.rect.x >= 700:
                    sch_1 +=1
            
               
            
        self.rect.x += self.speed
        self.rect.y += self.speed_1
        #if self.rect.x 
fon_t = pygame.font.SysFont("Arial", 25)
back = Spirt("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/p_back.png", 750, 500, 0, 0)
player = Player("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/gamer_1.png", 25, 88, 35+30, 150, 10)
player_1 = Player("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/gamer_2.png", 25, 88, 680-30, 150, 10)
balli = ball("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/ball.png", 50, 50, 250, 300, 10, 6)
clock = pygame.time.Clock()
game = True

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
    

    
    
    player.reset()
    player.wasd()
    player_1.reset()
    player_1.wasd_1()
    
    if pygame.sprite.collide_rect(player, balli) or pygame.sprite.collide_rect(player_1, balli):
        balli.speed *= -1
        
        if (balli.rect.y ==  player.top or balli.rect.y ==  player.botton) or (balli.rect.y ==  player_1.top or balli.rect.y ==  player_1.botton):
            balli.speed_1*=-1
           
    
    balli.wasd_2()
    win.blit(fon_t.render(("Красный: "+str(sch_1)) , True, (255, 0, 100)), (230, 5))
    win.blit(fon_t.render((" Vs. ") , True, (255, 255, 255)), (350, 5))
    win.blit(fon_t.render(("Зелёный: "+str(sch_2)), True, (0, 255, 0)), (400, 5))
    i = 10
    pygame.display.update()
    clock.tick(60)