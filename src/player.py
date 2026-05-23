import pygame
import os

class Player:
    def __init__(self):
        self.animations = {
            "Iddle" : pygame.image.load(os.path.join("assets", "images", "player", "iddle.png")).convert_alpha(),
            "Running" : [],
            "Jumping" : pygame.image.load(os.path.join("assets", "images", "player", "jumping.png")).convert_alpha(),
            "Caught" : pygame.image.load(os.path.join("assets", "images", "player", "caught.png")).convert_alpha()
        }
        self.frame = self.animations["Iddle"]
        self.state = "Iddle"
        self.current_frame = 0
        self.FRAME_WIDTH = 32
        self.FRAME_HEIGHT = 48
        running = pygame.image.load(os.path.join("assets", "images", "player", "running2.png")).convert_alpha()
        for i in range(running.width // self.FRAME_WIDTH):
            frame = running.subsurface((i* self.FRAME_WIDTH, 0, self.FRAME_WIDTH, self.FRAME_HEIGHT))
            self.animations["Running"].append(frame)

        self.char_rect = self.frame.get_rect()
        self.char_rect.width -= 10

        self.immunity = 0
        self.jump_strength = -10
        self.jump_limit = 1
        self.gravity = 0.5
        self.velocity_x = 5
        self.velocity_y = 0

        self.moving_right = False
        self.moving_left = False
        self.onground = False
        self.locked = False
        self.run_frames = []


    def jump(self):
        if self.jump_limit == 1 and self.locked == False:
            self.velocity_y += self.jump_strength
            self.jump_limit -= 1


    def move_x(self, map):
        if self.moving_right == True and self.locked == False :
            if self.char_rect.right >= map.LIMIT : 
                self.char_rect.right = map.LIMIT
            self.char_rect.x += self.velocity_x
        if self.moving_left == True and self.locked == False :
            if self.char_rect.x <= 0:
                return
            else :
                self.char_rect.x += - self.velocity_x

        collisions = map.get_tile_collisions(self.char_rect)
        for tile in collisions :
            if self.moving_right == True:
                self.char_rect.right = tile.left
            if self.moving_left == True:
                self.char_rect.left = tile.right

        self.handle_collisions(map)


    def move_y(self, map):
        self.velocity_y += self.gravity
        self.char_rect.y += self.velocity_y
        self.onground = False

        collisions = map.get_tile_collisions(self.char_rect)
        for tile in collisions:
            if self.velocity_y > 0:
                self.char_rect.bottom = tile.top
                self.velocity_y = 0
                self.onground = True
                self.jump_limit = 1
            elif self.velocity_y < 0:
                self.char_rect.top = tile.bottom
                self.velocity = 0

        self.handle_collisions(map)

    def handle_collisions(self, map) : 
        map.enemies.collisions(self)
        map.door_collisions(self.char_rect)
        map.collectibles.collisions(self.char_rect, map.current_level)


    def update_animation(self):
        if self.state == "Caught":
            return
        elif self.moving_left == True and self.moving_right == True:
            self.state = "Iddle"
        elif self.onground == False and self.velocity_y <= 0: 
            self.state = "Jumping"
        elif self.moving_left or self.moving_right:
            self.state = "Running"
        else:
            self.state = "Iddle"

    def unlock(self):
        self.locked = False
        self.immunity = 2
        self.state = "Iddle"

    def update(self, map, dt): 
        if self.immunity > 0:
            self.immunity -= dt
        self.move_x(map)
        self.move_y(map)
        self.update_animation()

    
    def running_frame(self):
        self.current_frame = (self.current_frame + 1) % len(self.animations["Running"])
        return self.current_frame



    def draw(self,screen, camera_x):
        if self.state == "Caught":
            self.frame = self.animations["Caught"]
        elif self.state == "Iddle":
            self.frame = self.animations["Iddle"]
        elif self.state == "Jumping" :
            self.frame = self.animations["Jumping"]
        elif self.state == "Running":
            self.running_frame()
            self.frame = self.animations["Running"][self.current_frame]

        image = self.frame

        if self.moving_left == True and self.state != "Caught" :
            image = pygame.transform.flip(image, True, False)

        screen.blit(image, 
                    (self.char_rect.x - camera_x, self.char_rect.y))



