import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

# carrega o gif animado usando a biblioteca movie
movie = pygame.movie.Movie("assets/images/passarinho.gif")

# obtém a superfície do gif
gif_surf = movie.get_surface()

# inicia a exibição do gif
movie.play()

# loop principal do jogo
while True:
    # processa eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # desenha a superfície do gif na tela
    screen.blit(gif_surf, (0, 0))
    pygame.display.update()
s