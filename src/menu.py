import pygame
import os

class Menu:
    def __init__(self):
        self.bg = pygame.image.load(os.path.join("assets", "images", "menu", "menu_bg.png"))
        self.options = [
            [pygame.image.load(os.path.join("assets", "images", "menu", "bt1.png")), (720, 330)],  # Commencer
            [pygame.image.load(os.path.join("assets", "images", "menu", "bt2.png")), (720, 500)], # Quitter
            [pygame.image.load(os.path.join("assets", "images", "menu", "unactive_bt.png")), (987, 645)] # Cinématiques
        ]
        self.cursor = pygame.image.load(os.path.join("assets", "images", "menu", "cursor.png"))
        self.active = 0
        self.cinematic = True
        self.font = pygame.font.SysFont("agencyfb", 24)
        self.command_key = pygame.image.load(os.path.join("assets", "images", "buttons", "a_key.png"))

        # Contient l'image, le moment d'affichage, le son correspondant, affichage
        self.title = [
            [pygame.image.load(os.path.join("assets", "images", "menu", "title1.png")), 0.5, pygame.mixer.Sound(os.path.join("assets", "audio", "sfx", "effect1.mp3")), False],
            [pygame.image.load(os.path.join("assets", "images", "menu", "title2.png")), 1.2, pygame.mixer.Sound(os.path.join("assets", "audio", "sfx", "effect1.mp3")), False],
            [pygame.image.load(os.path.join("assets", "images", "menu", "title3.png")), 2, pygame.mixer.Sound(os.path.join("assets", "audio", "sfx" ,"effect2.mp3")), False]
        ]

        # Fenêtre des commandes
        self.show_command = False
        self.box = pygame.Surface((550, 400))
        self.box.fill((51, 51, 51))
        self.command_img = [
            [pygame.image.load(os.path.join("assets", "images", "buttons", "arrows.png")), "Se déplacer"], 
            [pygame.image.load(os.path.join("assets", "images", "buttons", "space_key.png")), "Sauter"],
            [pygame.image.load(os.path.join("assets", "images", "buttons", "e_key.png")), "Valider"]
        ]

    def draw(self, screen, time):
        screen.blit(self.bg, (0,0))
        for image in self.options:
            screen.blit(image[0], (0,0))

        for word in self.title:
            if time > word[1] and word[3] == False:
                word[2].play()
                screen.blit(word[0])
                word[3] = True
            elif time > word[1]:
                screen.blit(word[0])

        screen.blit(self.cursor, self.options[self.active][1])
        animation_text = self.font.render("Passer les cinématiques", True, (51, 51, 51))
        screen.blit(animation_text, (1030, 678))
        screen.blit(self.command_key, (140, 662))
        command_text = self.font.render("Commandes", True, (51, 51, 51))
        screen.blit(command_text, (200, 678))

        if self.show_command == True :
            self.draw_commands(screen)

    # Dessine la fenêtre de commande si ouverte
    def draw_commands(self, screen):
            x = (screen.width - self.box.width ) / 2
            y = 200
            screen.blit(self.box, (x, y))
            white = (255, 255, 255)

            for i, img in enumerate(self.command_img):
                action = self.font.render(img[1], True, white)
                screen.blit(img[0], (x + 50, y + 90*(i+1)))
                screen.blit(action, (x + 375, y + 100*(i+1)))

    # Déplace le curseur
    def move_down(self):
        self.active += 1
        if self.active > len(self.options) - 1:
            self.active = 0

    def move_up(self):
        self.active -= 1
        if self.active < 0:
            self.active = len(self.options) - 1

    # Valide l'option pointée par le curseur :
        # Commencer le jeu
        # Quitter
        # Afficher / Passer les cinématiques
    def start(self, quit, cinematic, music):
        match self.active:
            case 0:
                music()
                cinematic()
            case 1 :
                quit()
            case 2:
                self.update_cinematics()

    def update_cinematics(self):
        if self.cinematic == True:
            self.cinematic = False
            self.options[2][0] = pygame.image.load(os.path.join("assets", "images", "menu", "active_bt.png"))
        else :
            self.cinematic = True
            self.options[2][0] = pygame.image.load(os.path.join("assets", "images", "menu", "unactive_bt.png"))

    def command_display(self):
        self.show_command = True

    def close_command(self):
        self.show_command = False

