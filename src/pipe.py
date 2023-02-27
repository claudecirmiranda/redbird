import pygame
import random

class Pipe:
    PIPE_WIDTH = 78
    PIPE_HEIGHT = 300
    PIPE_GAP = 60
    PIPE_SPEED = 6

    def __init__(self, x, y, screen, is_top_pipe):
        self.x = x
        self.y = y
        self.screen = screen
        self.is_top_pipe = is_top_pipe
        self.image = pygame.image.load("assets/images/pipe.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.PIPE_WIDTH, self.PIPE_HEIGHT))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = self.PIPE_SPEED
        self.passed = False

    def update(self):
        self.rect.x -= self.speed

        if self.is_top_pipe:
            self.rect.top = self.y
        else:
            self.rect.bottom = self.y + self.PIPE_GAP

    def render(self):
        self.screen.blit(self.image, self.rect)
