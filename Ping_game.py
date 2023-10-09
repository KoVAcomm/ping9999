import pygame
import random
pygame.init()
pygame.font.init()
sch_1 = 0
sch_2 = 0
cho = input("Вы хотите сражаться с ai (1) или с другим игроком (2)? (1/2): ")
flag_ai = False
if cho == "1":
    flag_ai = True
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
    def wasd_ai(self):
        if balli.rect.x > 300:
            if balli.rect.x >= 600:
                a = random.randint(-1, 1)
                self.rect.y += self.speed * a
            elif self.rect.y < 410 or self.rect.y > 0 and self.rect.y != balli.rect.y:
                if self.rect.y < balli.rect.y:
                    self.rect.y+=self.speed + random.randint(-5, 0)
                if self.rect.y > balli.rect.y:
                    self.rect.y-=self.speed+random.randint(-5, 0)
            

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
            if pygame.sprite.collide_rect(player, balli) or pygame.sprite.collide_rect(player_1, balli):
                balli.speed *= -1
            if (balli.rect.y ==  player.top or balli.rect.y ==  player.botton) or (balli.rect.y ==  player_1.top or balli.rect.y ==  player_1.botton):
                balli.speed_1*=-1
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
                if sch_1 == 50 or sch_2 == 50:
                    global win_n
                    win_n = True
        self.rect.x += self.speed
        self.rect.y += self.speed_1
pygame.display.set_icon(pygame.image.load("E:/Ping_999/ping.bmp"))
fon_t = pygame.font.SysFont("Arial", 25)
fon_t_1 = pygame.font.SysFont("Arial", 50)
back = Spirt("E:/Ping_999/p_back.png", 750, 500, 0, 0) 
player = Player("E:/Ping_999/gamer_1.png", 25, 88, 35+30, 190, 10)
player_1 = Player("E:/Ping_999/gamer_2.png", 25, 88, 680-30, 190, 10)
balli = ball("E:/Ping_999/ball.png", 50, 50, 250, 300, 10, 6)
table = Spirt("E:/Ping_999/table.png", 375, 60, 180, 5)
table_pob = Spirt("E:/Ping_999/table.png", 600, 96, 80, 180)
clock = pygame.time.Clock()
game = True
win_n = False
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Ping: 999")
i = 0
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    back.reset()
    if win_n == False:
        balli.reset()
        if i <= 0:
            flag_start = False
        player.reset()
        player.wasd()
        player_1.reset()
        if flag_ai:
            player_1.wasd_ai()
        else:
            player_1.wasd_1()
        
        balli.wasd_2()
        table.reset()
        win.blit(fon_t.render(("Красный: "+str(sch_1)) , True, (255, 0, 0)), (225, 20))
        win.blit(fon_t.render((" Vs. ") , True, (255, 255, 255)), (350, 20))
        win.blit(fon_t.render(("Зелёный: "+str(sch_2)), True, (0, 255, 100)), (400, 20))
        i = 10
    else:
        table_pob.reset()
        if sch_1 > sch_2:
            pob = fon_t_1.render("Победил Красный!", True, (255, 0, 0))
        elif sch_1 < sch_2:
            pob = fon_t_1.render("Победил Зелёный!", True, (0, 255, 100))
        else:
            pob = fon_t_1.render("Ничья", True, (255, 255, 255))
        win.blit(pob, (180, 200))
    pygame.display.update()
    clock.tick(60)