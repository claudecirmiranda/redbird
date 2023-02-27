import pygame
import sys


class GameOverScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score

    def show(self):
        title_font = pygame.font.SysFont(None, 60)
        score_font = pygame.font.SysFont(None, 30)
        title_text = title_font.render("Game Over", True, (255, 255, 255))
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return

            self.screen.fill((0, 0, 0))  # limpa a tela
            self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, 100))
            self.screen.blit(score_text, (self.screen.get_width() / 2 - score_text.get_width() / 2, 200))
            pygame.display.update()
