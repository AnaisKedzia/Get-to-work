import pygame
from src.player import Player
from src.level import Level
from src.camera import Camera
from src.qte import QTE
from src.menu import Menu
from src.cinematic import Cinematic
import os
from src.map_levels import bg_color, t_colors
from src.endscreen import Endscreen


class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 736))
        self.running = True
        self.FPS = 60
        self.font = pygame.font.SysFont("agencyfb", 24)

        self.menu = Menu()
        self.cinematics = Cinematic()
        self.player = Player()
        self.map = Level(self.screen.width, self.screen.height)
        self.endscreen = Endscreen(self.screen.width, self.screen.height)

        self.map.build_level()
        self.camera = Camera()
        self.qte = QTE(self.screen.width, self.screen.height)
        self.time_left = 90.0
        self.time_passed = 0
        self.GAME_STATE = "MENU"
        self.music = False
        self.timer_box = pygame.Surface((self.screen.width / 3, 20))

    def run(self):

        while self.running == True:
            dt = self.clock.tick(self.FPS) / 1000

            # Vérification des entrées
            self._check_events()

            # Actualisation des éléments
            if self.GAME_STATE == "MENU":
                self.time_passed += dt
                self.menu.draw(self.screen, self.time_passed)
                self.music_play()

            
            elif self.GAME_STATE == "CINEMATIC":
                self.cinematics.update(dt, self.map.current_level)
                self.cinematics.draw(self.screen, self.map.current_level)
                if self.map.current_level != 0 : self.music_play()


            elif self.GAME_STATE == "ENDING":
                self.endscreen.update(self.map.collectibles.skills, dt)
                self.endscreen.draw(self.screen, self.map.collectibles.skills)


            else : 
                if self.GAME_STATE == "PLAYING":
                    self.music_play()
                    self.player.update(self.map, dt)
                    self.camera.update(self.player, self.map, 
                                    self.screen.width)
                    if self.player.state == "Caught":
                        self.GAME_STATE = "QTE"
                        self.camera.shaking = True
            

                if self.GAME_STATE == "QTE":
                    self.qte.start_qte(self.map.current_level)
                    self.camera.shake()
                    if self.qte.active == False :
                        self.GAME_STATE = "PLAYING"
                        self.player.unlock()
                        self.map.enemies.active = self.map.enemies.char.get_rect()


                # Dessine les éléments sur l'écran
                self.map.draw_world(self.screen, self.camera.x)
                self.player.draw(self.screen, self.camera.x)
                if self.GAME_STATE == "QTE":
                    self.qte.draw(self.screen)

                self.time_left -= dt
                if self.time_left < 0:
                    self.qte.active = False
                    self.GAME_STATE = "PLAYING"
                    self.player.unlock()
                    self.next_level()
                self.render_timer()

            # Affichage des éléments
            pygame.display.flip()
            self.screen.fill(bg_color[self.map.current_level])
        
        self.running= False

    # Gestion des entrées utilisateurs
    def _check_events(self):
         for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.GAME_STATE=="PLAYING":
                self.handle_play_commands(event)
            elif self.GAME_STATE == "QTE":
                self.handle_qte_commands(event)
            elif self.GAME_STATE == "MENU" :
                self.handle_menu_commands(event)
            elif self.GAME_STATE == "CINEMATIC":
                self.handle_cinematic_commands(event)
            elif self.GAME_STATE == "ENDING":
                self.handle_endscreen(event)

    # Rendu du timer
    def render_timer(self):
        time_unit = (self.timer_box.width - 20) / 90
        timer = pygame.Surface((self.time_left * time_unit, 10))
        timer.fill(t_colors[self.map.current_level][1])

        self.timer_box.fill(t_colors[self.map.current_level][0])
        x = self.screen.width / 2 + self.timer_box.width / 2
        self.screen.blit(self.timer_box, (x, 0))
        self.screen.blit(timer, (x + 10, 5))

    def handle_play_commands(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                self.player.moving_left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.moving_right = True
            if event.key == pygame.K_SPACE :
                self.player.jump()
            if event.key == pygame.K_e and self.map.end_reached:
                self.next_level()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                self.player.moving_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.moving_right = False

    def handle_qte_commands(self, event):
        if event.type == pygame.KEYDOWN:
            self.qte.check_keys(event.key)

    def handle_menu_commands(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e :
                self.menu.start(self.quit, self.cinematic, self.music_off)
            if event.key == pygame.K_UP or event.key == pygame.K_z:
                self.menu.move_up()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s :
                self.menu.move_down()
            if event.key == pygame.K_a :
                self.menu.command_display()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.menu.close_command()
        
    def handle_cinematic_commands(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and self.map.current_level == 0 :
                self.cinematics.advance(self.cinematic, True, self.add_level)
            elif event.key == pygame.K_e : 
                self.cinematics.advance(self.play, False, self.add_level)

    def handle_endscreen(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e :
                for i in range(len(self.menu.title)):
                    self.menu.title[i][3] = False
                self.GAME_STATE = "MENU"
                self.player = Player()
                self.map = Level(self.screen.width, self.screen.height)
                self.endscreen = Endscreen(self.screen.width, self.screen.height)
                self.map.build_level()
                self.camera = Camera()
                self.time_passed = 0
                self.time_left = 90.0
                self.endscreen = Endscreen(self.screen.width, self.screen.height)
                pygame.mixer.stop()

    def add_level(self):
        self.map.current_level += 1
        self.map.collectibles.create_counter(self.map.current_level)

    def next_level(self):
        if self.map.current_level == 5:
            self.music_off()
            self.GAME_STATE = "ENDING"
        else :
            self.map.load_level(self.player, self.camera)
            self.music = False
            self.cinematic()
            self.time_left = 90.0

    def quit(self):
        self.running = False

    def play(self):
        self.GAME_STATE = "PLAYING"
        self.time_passed = 0

    def cinematic(self):
        if self.menu.cinematic == True :
            self.GAME_STATE = "CINEMATIC"
        else:
            if self.map.current_level == 0 :
                self.map.current_level +=1
                self.map.collectibles.create_counter(self.map.current_level)
            self.play()

    def music_off(self):
        self.music = False
        pygame.mixer.music.stop()

    def music_play(self):
        pygame.mixer.music.set_volume(0.5)
        if self.GAME_STATE == "MENU" and self.music == False and self.time_passed > 3:
            pygame.mixer.music.load(os.path.join("assets", "audio", "music", "menu.mp3"))
            pygame.mixer.music.play(-1)
            self.music = True
        elif (self.GAME_STATE == "PLAYING" or self.GAME_STATE == "CINEMATIC") and self.music == False: 
            pygame.mixer.music.load(os.path.join("assets", "audio", "music", f"level{self.map.current_level}.mp3"))
            pygame.mixer.music.play(-1)
            self.music = True


game = Game()
game.run()