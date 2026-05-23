import pygame
from src.map_levels import text, cinematic, titles
import os

class Cinematic() : 
    def __init__(self):
        self.font = pygame.font.SysFont("agencyfb", 22)
        self.color = (255, 255, 255)
        self.curr_index = 0
        self.displayed_text = ""
        self.full_text = ""

        self.timer = 0
        self.text_speed = 0.02
        self.e_key = pygame.image.load(os.path.join("assets", "images", "buttons", "e_key.png"))
        self.e_key = pygame.transform.scale(self.e_key, (25, 25))

    def update(self, dt, level):
        self.timer += dt
        if self.full_text == "":
            self.full_text = text[level]

        if self.timer >= self.text_speed and self.curr_index < len(self.full_text):
            self.timer = 0
            self.curr_index += 1
            self.displayed_text = self.full_text[:self.curr_index]


    def draw(self, screen, level):
        screen.fill((0, 0, 0))

        if level == 0:
            font = pygame.font.SysFont("agencyfb", 30)
            intro = font.render(self.displayed_text, True, (255, 255, 255))
            screen.blit(intro, (20, 150))
            if len(self.displayed_text) == len(self.full_text):
                screen.blit(self.e_key, (screen.width - 75, screen.height - 75))

        elif level > 0:
            intro = self.font.render(self.displayed_text, True, (255, 255, 255))
            title = self.font.render(titles[level], True, (255, 255, 255))
            img = cinematic[level]
            x = (screen.width - img.width) / 2 
            screen.blit(img, (x , 0))
            
            box = self.create_box(img.width, img.height)
            screen.blit (box, (x , img.height))

            screen.blit(title, (x +25, img.height + 25))
            screen.blit(intro, (x + 50, img.height + 75))

            if len(self.displayed_text) == len(self.full_text):
                screen.blit(self.e_key, (img.width + 125, screen.height - 50))

    # Passe la cinématique ou affiche le texte dans sa totalité
    def advance(self, play, intro, add):
        if self.displayed_text < self.full_text:
            self.displayed_text = self.full_text
            self.curr_index = len(self.full_text)
        else:
            play() 
            self.displayed_text = ""
            self.full_text = ""
            self.curr_index = 0
            if intro == True: add()

    def create_box(self, width, height):
        box = pygame.Surface((width, height))
        box.fill((50, 50, 50))
        return box
