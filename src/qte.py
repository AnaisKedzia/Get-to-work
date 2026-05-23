import pygame
import os
import random
from src.map_levels import custom_window

class QTE() :
    def __init__(self, width, height):
        self.WIDTH = 64
        self.HEIGHT = 64
        self.assets = pygame.image.load(os.path.join("assets", "images", "buttons", "arrows.png"))
        self.cursor = pygame.image.load(os.path.join("assets", "images", "buttons", "hand.png"))
        self.arrows = []
        self.active = False
        for i in range(self.assets.width // self.WIDTH):
            arrow = self.assets.subsurface((i * self.WIDTH, 0, self.WIDTH, self.HEIGHT))
            self.arrows.append(arrow)

        self.arrows_match = {
            "Up" : 0,
            "Right" : 1,
            "Down" : 2,
            "Left" : 3
        }
        self.level = 2
        self.bg_colors = [(242, 250, 255),(245, 238, 218),(255, 255, 255),(0,0,0)]
        self.sfx_caught = pygame.mixer.Sound(os.path.join("assets", "audio", "sfx", "caught.mp3"))

        self.combination = []
        self.input = []

        self.display_window = pygame.Surface((width // 2, height //2))
        self.display_rect = pygame.Rect(width // 4, height //4,
                            self.display_window.width, self.display_window.height)
        self.arrows_rect = []
        for i in range(4):
            rect = pygame.Rect(
                    self.display_rect.x + self.display_rect.width // 4 * i + self.display_rect.width // 8 - self.WIDTH // 2,
                    self.display_rect.y + self.display_rect.height // 2 - self.HEIGHT // 2,
                    self.WIDTH, self.HEIGHT
                )
            self.arrows_rect.append(rect)
        
    # Création d'une combinaison aléatoire
    def random_combination(self):
        for _ in range(4):
            x = random.randrange(0,4)
            self.combination.append(x)
        self.active = True

    # Initialisation du QTE 
    def start_qte(self, level):
        if self.active == False :
            self.random_combination()
            self.sfx_caught.play()
            self.level = level
            self.window = custom_window[level]

        self.check_match()

    # Comparaison des entrées et la combinaison
    def check_match(self):
        key_num = len(self.input) - 1
        if len(self.input) <= 4 and len(self.input) != 0:
            entry, combination = self.input[key_num], self.combination[key_num]
            if entry != combination :
                self.input = [] 
            elif self.input == self.combination and len(self.input) != 0:
                self.active = False
                self.combination = []
                self.input = []


    def draw(self,screen):
        display = pygame.Surface((screen.width // 2, screen.height //2))
        display.fill(self.bg_colors[self.level - 2])
        screen.blit(display, (screen.width // 4, screen.height //4))
        screen.blit(self.window, (screen.width // 4 -40, screen.height //4 -24))
        if len(self.input) < 4 :
            screen.blit(self.cursor,(self.arrows_rect[len(self.input)].x, self.arrows_rect[0].y - 64))

        for i,rect in enumerate(self.arrows_rect) :
            screen.blit(self.arrows[self.combination[i]], (rect.x, rect.y))

    def check_keys(self, event):
        match event : 
            case pygame.K_UP:
                self.input.append(self.arrows_match["Up"])
            case pygame.K_RIGHT:
                self.input.append(self.arrows_match["Right"])
            case pygame.K_DOWN:
                self.input.append(self.arrows_match["Down"])
            case pygame.K_LEFT:
                self.input.append(self.arrows_match["Left"])


        



