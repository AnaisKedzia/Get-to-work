import os
import pygame

class Collectibles():
    def __init__(self, level):
        self.items = []
        self.HEIGHT = 32
        self.WIDTH = 32
        self.item_counters = []
        self.font = pygame.font.SysFont("agencyfb", 16)

        # Compétence, compteur, image correspondante
        self.skills = {
            1 : ["Management", 0, pygame.image.load(os.path.join("assets", "images", "skills", "management.png"))],
            2 : ["Korean", 0, pygame.image.load(os.path.join("assets", "images", "skills", "korean.png"))],
            3 : ["Energy", 0, 
                   [pygame.image.load(os.path.join("assets", "images", "skills", "carrot.png")), pygame.image.load(os.path.join("assets", "images", "skills", "milk.png")), pygame.image.load(os.path.join("assets", "images", "skills", "egg.png"))]],
            4 : ["Programming", 0, [pygame.image.load(os.path.join("assets", "images", "skills", "js.png")), pygame.image.load(os.path.join("assets", "images", "skills", "css.png")), pygame.image.load(os.path.join("assets", "images", "skills", "py.png"))]],
            5 : ["ISTQB", 0, pygame.image.load(os.path.join("assets", "images", "skills", "istqb.png"))]
        }
        self.create_counter(level)
        self.sfx__collect = pygame.mixer.Sound(os.path.join("assets", "audio", "sfx", "collect.mp3"))
        self.sfx__collect.set_volume(0.5)

    # Création des coordonnées d'un objet et ajout à la liste des objets
    def create_item(self, x, y):
        item = pygame.Rect(x, y, self.HEIGHT, self.WIDTH)
        self.items.append(item)

    # Création des coordonnées d'un objet et ajout à une sous-liste (level 3/4)
    def create_items(self, x, y):
        if len(self.items) == 0 : 
            self.items = [[], [], []]

        item = pygame.Rect(x, y, self.HEIGHT, self.WIDTH)

        for sub_list in self.items :
            if len(sub_list) < 3 :
                sub_list.append(item)
                break

    # Création des Rectangles pour l'affichage du nombre d'items
    def create_counter(self, level):
        self.item_counters = []
        for i in range(level):
            rect = pygame.Rect(0, 0, self.HEIGHT, self.WIDTH)
            rect.x = 2 * i * rect.width
            self.item_counters.append(rect)

    def collisions(self, player, level):
        if level == 3 or level == 4:
            for sub_list in self.items:
                for item in sub_list :
                    if player.colliderect(item):
                        self.sfx__collect.play()
                        sub_list.remove(item)
                        self.skills[level][1] += 1
        else : 
            for item in self.items:
                if player.colliderect(item):
                    self.sfx__collect.play()
                    self.items.remove(item)
                    self.skills[level][1] += 1
    
    def draw(self, screen, camera_x, level):
        if level == 3 or level == 4 : 
            for n, sub_list in enumerate(self.items) : 
                for item in sub_list : 
                    image =  self.skills[level][2][n]
                    screen.blit(image, (item.x - camera_x, item.y))
        else :
            for item in self.items :
                    image = self.skills[level][2]
                    screen.blit(image, (
                            item.x - camera_x, item.y
                        ))
        
        color = self.get_color(level)

        # Affiche le nombre d'items obtenu
        for i, counter in enumerate(self.item_counters):
            level = i +1
            if i == 2 or i == 3 : 
                screen.blit(self.skills[level][2][0], (counter.x, counter.y))
                text = self.font.render(f"x {int(self.skills[i+1][1])}", True, color)
                screen.blit(text, (counter.x + 32, 10))
            else :
                screen.blit(self.skills[level][2], (counter.x, counter.y))
                text = self.font.render(f"x {int(self.skills[level][1])}", True, color)
                screen.blit(text, (counter.x + 32, 10))
            
        

    def get_color(self, level):
        if level == 5 :
            return (255, 255, 255)
        else :
            return (0, 0, 0)