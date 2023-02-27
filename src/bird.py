import pygame

class Bird(pygame.sprite.Sprite):
    GRAVITY = 0.25
    FLAP_SPEED = 5

    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.velocity = 0

        # carrega o arquivo de imagem animada
        self.images = []
        for i in range(1, 6):
            img = pygame.image.load(f"assets/images/birds/bird{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (70, 65))
            self.images.append(img)

        # define a animação
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.frame = 0
        self.animation_speed = 0.1

    def flap(self):
        self.velocity = -self.FLAP_SPEED

    def update(self):
        self.velocity += self.GRAVITY
        self.y += self.velocity
        self.rect.center = (self.x, self.y)

        # atualiza a animação
        self.frame += self.animation_speed
        if self.frame >= len(self.images):
            self.frame = 0
        self.image = self.images[int(self.frame)]

    def render(self):
        self.screen.blit(self.image, self.rect)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.rect.center = (self.x, self.y)
