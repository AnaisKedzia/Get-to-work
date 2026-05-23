import pygame
from src.map_levels import levels, tiles, caught
import os
from src.enemy import Enemy
from src.collectibles import Collectibles

class Level: 
    def __init__(self, width, height):
        self.TILE_SIZE = 32
        self.tiles = []
        self.current_level = 0
        self.level_tiles = tiles[1]
        self.enemies = Enemy()
        self.collectibles = Collectibles(self.current_level)
        self.map = levels[1]
        self.door = tiles["door"]
        self.door_rect = pygame.Rect((width * 3) - (5 * self.TILE_SIZE),
                         height - (2*self.TILE_SIZE + self.enemies.HEIGHT),
                        self.door.width, self.door.height)
        self.end_reached = False
        self.current_room = 0
        self.LIMIT = width * 3 - 5
        self.e_key = pygame.image.load(os.path.join("assets", "images", "buttons", "e_key.png"))
        self.e_key = pygame.transform.scale(self.e_key, (25, 25))

    def build_level(self):
        for row_index, row in enumerate(self.map):
            for col_index, tile in enumerate(row):
                if tile == "X" or "O" or "Y":
                    x = self.TILE_SIZE * col_index
                    y = self.TILE_SIZE * row_index
                    if tile == "X":
                        block = pygame.Rect(x, y, self.TILE_SIZE, self.TILE_SIZE) 
                        self.tiles.append([block, "X"])
                    elif tile =="O":
                        block = pygame.Rect(x, y, self.TILE_SIZE, self.TILE_SIZE) 
                        self.tiles.append([block, "O"])
                    elif tile == "Y":
                        y += self.TILE_SIZE - self.enemies.HEIGHT
                        self.enemies.create_enemy(x,y)
                    elif tile == "C":
                        if self.current_level == 3 or self.current_level == 4 : 
                            self.collectibles.create_items(x, y)
                        else : 
                            self.collectibles.create_item(x,y)

    # Charge le prochain niveau
    def load_level(self, player, camera):
        self.current_level += 1
        self.map = levels[self.current_level]
        self.level_tiles = tiles[self.current_level]

        # Réinitialisation des éléments
        player.char_rect.x = 0
        player.char_rect.y = 0
        player.moving_right, player.moving_left = False, False
        camera.x = 0
        player.animations["Caught"] = caught[self.current_level]
        self.tiles = []
        self.enemies.enemies = []
        self.collectibles.items = []
        self.collectibles.create_counter(self.current_level)
        
        self.build_level()


    def get_tile_collisions(self, player):
        return [tile[0] for tile in self.tiles if player.colliderect(tile[0])]


    def door_collisions(self, player):
        if player.colliderect(self.door_rect) : 
            self.end_reached = True
        else : 
            self.end_reached = False


    def draw_world(self, screen, camera_x):
        for tile in self.tiles:
            if tile[1] == "X":
                screen.blit(self.level_tiles[0], 
                            (tile[0].x - camera_x, tile[0].y))
            elif tile[1] == "O":
                screen.blit(self.level_tiles[1], 
                    (tile[0].x - camera_x, tile[0].y))
        screen.blit(self.door, (self.door_rect.x - camera_x, self.door_rect.y))
        self.enemies.draw(screen, camera_x, self.current_level)
        self.collectibles.draw(screen, camera_x, self.current_level)

        if self.end_reached == True:
            screen.blit(self.e_key, (screen.width - 50, screen.height - 35))
        
        
