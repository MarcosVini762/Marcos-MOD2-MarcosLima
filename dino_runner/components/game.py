import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 12
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True         #ESSA FUNCTION SETA UM VALOR TRUE EM RUNNING 
        while self.running:         #QUE SE O PLAYER 
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True                         #Esse bloco aqui reseta e inicializa tudo, trazendo a velocidade do jogo
        self.obstacle_manager.reset_obstacles()     #para a velocidade do começo tento em vista, o recomeço ou até a primeira interação
        self.power_up_manager.reset_power_ups()
        self.game_speed = 12
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():   # Esse bloco tem o ojetivo de fazer o botão de 'SAIR' do jogo
            if event.type == pygame.QUIT:  # tendo em vista que a janela do jogo não tem essa função 
                self.playing = False       # isso é feito adicionando um evento chamado 'QUIT'
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()                                  # O update é muitas vezes chamado durante o código
        self.player.update(user_input)                                         # se tornando muito importante pois ele 'atualiza'
        self.obstacle_manager.update(self)                                     # tudo oque foi alterado, pois durante o andamento do jogo
        self.update_score()                                                    # o mesmo sofre inumeras alterações, como por exemplo o score
        self.power_up_manager.update(self.score, self.game_speed, self.player) # que é constantemente atualizado e exibido na tela 

    def update_score(self):
        self.score += 1                    # O update score, como o proprio nome já diz ele tem como função 'atualizar'
        if self.score % 100 == 0:          # a pontuação do score, e ao mesmo tempo ele pega esse valor e incrementa
            self.game_speed += 2           # visando aumentar a velocidade do jogo assim dificultando um pouco o jogo

    def draw(self):
        self.clock.tick(FPS)                    # Essa função tem como objetivo desenhar todos os elementos do jogo na tela
        self.screen.fill((255, 255, 255))       # e no final dela exite um update, que meio que atualiza tudo e joga no display
        self.draw_background()                  # sem o update as imagens ficariam paradas, pois elas não seriam alteradas pelos eventos
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))                # Essa função tem como objetivo causar a impresão de que o fundo está em movimento
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))  # ela meio que rola a imagem, causando essa impressão 
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
         draw_message_component(        # Essa função desenha um contador de pontos no canto superior direito da tela
            f"Score: {self.score}",     # realizando a contagem de pontos do usuário
            self.screen,
            pos_x_center=1000,
            pos_y_center=50
        )   

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((246, 143, 70))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
           draw_message_component("Press any key to start", self.screen)
        else:
            draw_message_component("Press any key to restart", self.screen, pos_y_center=half_screen_height + 140)
            draw_message_component(
                f"Your Score: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )            
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 100
            )
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 30))

        pygame.display.flip()

        self.handle_events_on_menu()
