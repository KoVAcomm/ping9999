import pygame
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
back = Spirt("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/p_back.png", 750, 500, 0, 0)
player = Player("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/gamer_1.png", 25, 88, 35, 150, 5)
player_1 = Player("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/gamer_2.png", 25, 88, 680, 150, 5)
clock = pygame.time.Clock()
game = True
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Ping: 9999")
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    back.reset()
    player.reset()
    player.wasd()
    player_1.reset()
    player_1.wasd_1()
    pygame.display.update()
    clock.tick(60)