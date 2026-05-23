import pygame
import os
import random

class Endscreen:
    def __init__(self, width, height):
        self.bg = pygame.image.load(os.path.join("assets", "images", "endscreen", "ending.png"))
        self.resume = pygame.image.load(os.path.join("assets", "images", "endscreen", "resume.png"))
        self.score_window = pygame.Surface((width / 2, height))
        self.score_window.fill((55, 55, 55))
        self.score_window.set_alpha(250)
        self.resume_rect = self.resume.get_rect()
        self.resume_rect.x = width

        self.sliding_speed = 7
        self.fill_speed = 3
        self.target_x = width / 1.6
        self.calculation_finished = False
        self.result = "Unknown"
        self.time_passed = 0

        self.effect = pygame.mixer.Sound(os.path.join("assets", "audio", "sfx", "filling.mp3"))
        self.effect.set_volume(0.4)
        self.effect2 = pygame.mixer.Sound(os.path.join("assets", "audio", "sfx", "effect2.mp3"))
        self.played = False
        self.played2 = False

        self.score_bar = pygame.image.load(os.path.join("assets", "images", "endscreen", "scorebar2.png"))
        self.m = pygame.image.load(os.path.join("assets", "images", "endscreen", "bar.png"))
        self.stamp = None


        # Position, remplissage des barres
        self.bars = [
            [(995, 155), 0],
            [(995, 250), 0],
            [(690, 100), 0],
            [(995, 370), 0],
            [(995, 490), 0]
            ]
        self.font = pygame.font.SysFont("agencyfb", 18)
        self.font2 = pygame.font.SysFont("agencyfb", 30)
        self.motivation = self.font.render("Motivation", True, (255,255,255))

        self.button = pygame.image.load(os.path.join("assets", "images", "buttons", "e_key.png"))
        self.button = pygame.transform.scale(self.button, (35, 35))

    def draw(self, screen, counts):
        self.update_resume()


        screen.blit(self.bg, (0, 0))
        screen.blit(self.score_window, (screen.width/2, 0))
        screen.blit(self.resume, (self.resume_rect.x, 50))

        # Dessine les barres de score une fois le cv affiché
        if self.resume_rect.x <= self.target_x :
            self.draw_score(screen, counts)

        if self.time_passed > 0.7 and self.calculation_finished == True:
            if self.played2 == False : 
                self.effect2.play()
                self.played2 = True
            screen.blit(self.stamp, (0, 0))
            screen.blit(self.button, (50, screen.height - 100))
            text = self.font2.render("Menu", True, (51, 51, 51))
            screen.blit(text, (100, screen.height - 100))



    def update_resume(self):
        if self.resume_rect.x >=  self.target_x :
            self.resume_rect.x -= self.sliding_speed


    def draw_score(self, screen, counter):
        if self.calculation_finished == False and self.bars[0][1] == 0 and self.played == False:
            self.effect.play(-1)
            self.played = True


        for i in range(len(counter)):

            x, y = self.bars[i][0]

            # Affichage et animation des barres de score basiques
            if i != 2:
                # Création de la barre actuelle
                limit = counter[i+1][1] * int((self.score_bar.width - 10 ) / 9)
                width = self.bars[i][1]
                bar = pygame.Surface((width, 19))
                bar.fill((53, 135, 87))

                # Actualise le remplissage de la barre
                if width < limit : 
                    self.bars[i][1] += self.fill_speed
                    screen.blit(bar, (x + 7, y + 24))
                    screen.blit(self.score_bar,(x, y))
                    break

                # Stocke la barre quand la limite est atteinte
                else :
                    self.bars[i].append(bar)

            # Affichage et animation de la barre de motivation
            else : 
                limit = counter[i+1][1] * int((self.m.height) / 9)
                height = self.bars[i][1]
                bar = pygame.Surface((49,height))
                bar.fill((53, 135, 87))

                if height < limit:
                    self.bars[i][1] += self.fill_speed *3
                    screen.blit(bar, (x, y + self.m.height - height))  
                    screen.blit(self.m, (x, y))
                    screen.blit(self.motivation, (x - 5, y + 20 + self.m.height))
                    break
                else : 
                    self.bars[i].append(bar)


            # Affichage des barres déjà animées
            for n in range(i + 1):
                if n == 2 : 
                    x, y = self.bars[n][0]
                    screen.blit(self.bars[n][2], (x, y + self.m.height - height))
                    screen.blit(self.m, (x, y))
                    screen.blit(self.motivation, (x -5, y + 20 + self.m.height))
                else : 
                    x, y = self.bars[n][0]
                    screen.blit(self.bars[n][2], (x + 7, y + 24))
                    screen.blit(self.score_bar, self.bars[n][0])
        
        # Fin de l'animation
        if i == 4 and width >= limit:
            self.calculation_finished = True
            self.effect.stop()

# Calcul du résultat final
    def calculate_win(self, skills) : 
        if self.result == "Unknown":
            win_rate = 0
            for skill in skills:
                win_rate += int(skills[skill][1] * 1.888)
                
            target = random.randrange(0, 100)
            if win_rate >= target:
                self.result = "Win"
            else:
                self.result = "Lose"

        
    def update(self, skills, dt):
        if self.result == "Unknown":
            self.calculate_win(skills)
        
        if self.calculation_finished == True : 
            self.time_passed += dt
            if self.result == "Lose" and self.stamp == None :
                self.bg = pygame.image.load(os.path.join("assets", "images", "endscreen", "rejected_bg.png"))
                self.stamp = pygame.image.load(os.path.join("assets", "images", "endscreen", "rejected.png"))
            elif self.result == "Win" and not hasattr(Endscreen, "tampon"):
                self.bg = pygame.image.load(os.path.join("assets", "images", "endscreen", "hired_bg.png"))
                self.stamp = pygame.image.load(os.path.join("assets", "images", "endscreen", "hired.png"))

