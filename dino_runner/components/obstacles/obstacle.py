import random

from ctypes.wintypes import SC_HANDLE
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image 
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

    def when_hammer_colliderect_obstacle(self, player):
        self.hammer = True
        for power_up in self.power_ups:
            if player.dino_rect.colliderect(self.hammer):
                #self.power_ups.remove(power_up)
                pass