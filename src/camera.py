
class Camera():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 32
        self.target_x = 0
        self.sliding = False
        self.shaking = False
        self.effect_t = 1

    def update(self, player, map, width):
        self.target_x = map.current_room * width
        if (player.char_rect.right > (map.current_room + 1) * width) :
            map.current_room += 1
            player.locked = True
            self.sliding = True

        elif (player.char_rect.left < map.current_room * width - player.char_rect.width) : 
            map.current_room -= 1
            self.sliding = True
            player.locked = True

        self.slide(player)

    def slide(self, player):
        if self.sliding:
            if self.x < self.target_x :
                self.x += self.speed
                if self.x >= self.target_x:
                    self.x = self.target_x
                    self.sliding = False
                    player.locked = False
            elif self.x > self.target_x:
                self.x -= self.speed
                if self.x <= self.target_x:
                    self.x = self.target_x
                    self.sliding = False
                    player.locked = False

    def shake(self):
        if self.shaking == True and self.effect_t < 5 :
            self.x += 10 + (- 20 * (self.effect_t % 2))
            self.effect_t += 1
        else : 
            self.shaking = False
            self.effect_t = 1

        
