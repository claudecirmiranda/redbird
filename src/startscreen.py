import pygame
import sys


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        
    def show(self):
        pygame.font.init()
        title_font = pygame.font.Font("assets/fonts/04B_19.ttf", 36)
        start_font = pygame.font.SysFont(None, 30)
        title_text = title_font.render("Red Bird", True, (186, 2, 2))
        start_text = start_font.render("Pressione 'espaço' para começar", True, (166, 2, 2))
        start_esc =  start_font.render("   Pressione 'Esc' para sair   ", True, (166, 2, 2))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, 50))
            self.screen.blit(start_text, (self.screen.get_width() / 2 - start_text.get_width() / 2, 150))
            self.screen.blit(start_esc, (self.screen.get_width() / 2 - start_text.get_width() / 2, 200))
            pygame.display.update()
