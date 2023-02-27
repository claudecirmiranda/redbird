import random
import sys
import pygame
from .bird import Bird
from .pipe import Pipe
from .startscreen import StartScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.screen = pygame.display.set_mode((771, 432))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("assets/fonts/OpenSans-Regular.ttf", 20)
        self.fontgo = pygame.font.Font("assets/fonts/04B_19.ttf", 36)
        self.background = pygame.image.load("assets/images/backgrounds/background2.png").convert()
        self.bird = Bird(50, self.screen.get_height() / 2 - 12, self.screen)
        self.pipes = []
        self.score = 0
        self.is_game_over = False
        self.spawn_pipe()

    def reset(self):
        self.bird.reset(50, self.screen.get_height() / 2)
        self.pipes = []
        self.score = 0
        self.create_pipe_timer = pygame.time.get_ticks()
        self.last_pipe_created = False
        self.is_game_over = False
        self.show_score = True
        self.reset_game=True
        self.run()

    def spawn_pipe(self):
        """Adiciona um novo cano à lista de canos."""
        # Define a posição x do novo cano.
        x = self.screen.get_width() + Pipe.PIPE_WIDTH // 2

        # Define a posição y do cano inferior.
        bottom_pipe_y = random.randint(350, 480)

        # Adiciona um novo cano inferior à lista de canos.
        bottom_pipe = Pipe(x, bottom_pipe_y, self.screen, is_top_pipe=False)
        self.pipes.append(bottom_pipe)

        # Define a posição y do cano superior.
        pipe_gap_height = Pipe.PIPE_GAP + 2 * Pipe.PIPE_HEIGHT
        top_pipe_y = bottom_pipe_y - pipe_gap_height
        
        # Adiciona um novo cano superior à lista de canos.
        is_top_pipe = True
        top_pipe = Pipe(x, top_pipe_y, self.screen, is_top_pipe=is_top_pipe)
        top_pipe.image = pygame.transform.flip(top_pipe.image, False, True)
        self.pipes.append(top_pipe)

    def show_game_over_screen(self):
        """Mostra a tela de fim de jogo."""
        # Define a fonte para o texto de fim de jogo.
        pygame.font.init()
        font = pygame.font.Font("assets/fonts/04B_19.ttf", 36)
        # Renderiza o texto de fim de jogo.
        game_over_text = font.render("Game Over", True, (0, 0, 0))
        # Renderiza o texto para jogar novamente.
        retry_text = font.render("Jogar novamente", True, (0, 0, 0))
        # Renderiza o texto para sair do jogo.
        quit_text = font.render("Sair", True, (0, 0, 0))

        # Define as posições dos textos na tela.
        game_over_text_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, 50))
        retry_text_rect = retry_text.get_rect(center=(self.screen.get_width() // 2, 150))
        quit_text_rect = quit_text.get_rect(center=(self.screen.get_width() // 2, 250))

        # Mostra os textos na tela.
        self.screen.blit(game_over_text, game_over_text_rect)
        self.screen.blit(retry_text, retry_text_rect)
        self.screen.blit(quit_text, quit_text_rect)

        # Atualiza a tela.
        pygame.display.flip()

        while True:
            # Aguarda um evento do usuário.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Sai do jogo.
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if retry_text_rect.collidepoint(mouse_pos):
                        # Reinicia o jogo.
                        self.reset()
                        #return
                    elif quit_text_rect.collidepoint(mouse_pos):
                        # Sai do jogo.
                        pygame.quit()
                        sys.exit()

    def check_collision(self):
        """Verifica se o pássaro colidiu com algum cano."""
        for pipe in self.pipes:
            if self.bird.rect.colliderect(pipe.rect):
                return True
        return False

    def check_score(self):
        for pipe in self.pipes:
            if pipe.is_top_pipe and pipe.rect.right < self.bird.rect.left and not pipe.passed:
                pipe.passed = True
                return True
        return False

    PIPE_SPAWN_INTERVAL = 1500  # em milissegundos

    def run(self):

        if not self.is_game_over:
            StartScreen.show(self)

        self.pipe_spawn_timer = pygame.time.get_ticks()

        while not self.is_game_over:
            current_time = pygame.time.get_ticks()

            if self.is_game_over:
                    self.show_start_screen(reset_game=True)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()

            # verifica se é hora de gerar um novo cano
            if current_time - self.pipe_spawn_timer > Game.PIPE_SPAWN_INTERVAL:
                self.spawn_pipe()
                self.pipe_spawn_timer = current_time
                
            self.screen.blit(self.background, (0, 0))

            # renderiza e atualiza a posição dos tubos
            for pipe in self.pipes:
                pipe.render()
                pipe.update()

            # renderiza e atualiza a posição do pássaro
            self.bird.render()
            self.bird.update()

            # verifica se o pássaro colidiu com algum tubo
            if self.check_collision():
                self.is_game_over = True

            # verifica se o pássaro passou por um tubo
            if self.check_score():
                self.score += 1

            # renderiza a pontuação na tela
            score_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_surface, (10, 10))

            pygame.display.update()
            self.clock.tick(60)

        #pygame.quit()
        self.show_game_over_screen()
        
