from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS


class  ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0 :
            small_cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(small_cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
