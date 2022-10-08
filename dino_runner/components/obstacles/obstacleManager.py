import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class  ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0 :
            small_cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(small_cactus)
            #if len(self.obstacles) == 1:
                #large_cactus = Cactus(LARGE_CACTUS)
                #self.obstacles.append(large_cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count +=1
                else:
                    self.obstacles.remove(obstacle)
            break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
        
