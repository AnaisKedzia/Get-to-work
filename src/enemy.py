import pygame
import os
from src.map_levels import enemies

class Enemy():
    def __init__(self):
        self.enemies = []
        self.char = pygame.image.load(os.path.join("assets", "images", "ennemies", "enemy1.png"))
        self.HEIGHT = 48
        self.WIDTH = 32
        self.active = pygame.Rect(0, 0, 0, 0)


    def draw(self, screen, camera_x, level):
        if len(self.enemies) != 0: 
            image = enemies[level]
            for enemy in self.enemies :
                if enemy.x == self.active.x and enemy.y == self.active.y:
                    pass
                else :
                    screen.blit(image, (
                        enemy.x - camera_x, enemy.y
                    ))

    def create_enemy(self, x, y):
        block = pygame.Rect(x, y, self.WIDTH - 10, self.HEIGHT)
        self.enemies.append(block)

    def collisions(self, player):
        for enemy in self.enemies : 
            if player.char_rect.colliderect(enemy) and player.immunity <= 0 :
                self.active = enemy
                player.state = "Caught"
                player.locked = True
                player.moving_right, player.moving_left = False, False

