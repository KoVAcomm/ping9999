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

back = Spirt("C:/Users/guest/OneDrive/Рабочий стол/Ping_999/p_back.png", 750, 500, 0, 0)
clock = pygame.time.Clock()
game = True
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Ping: 9999")
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    back.reset()
    pygame.display.update()
    clock.tick(60)