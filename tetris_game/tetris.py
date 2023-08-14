import pygame
import sys
from .game import Game
from .colors import Colors

class Tetris:
    def __init__(self):
        self.bootstrap()

        self.title_font = pygame.font.Font(None, 40)
        self.score_surface = self.title_font.render(
            "SCORE", True, Colors.white)
        self.next_surface = self.title_font.render("NEXT", True, Colors.white)
        self.game_over = self.title_font.render(
            "GAME OVER", True, Colors.white)

        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.next_rect = pygame.Rect(320, 215, 170, 180)

        self.screen = pygame.display.set_mode((500, 620))
        pygame.display.set_caption('Tetris')

        self.game = Game()

        self.clock = pygame.time.Clock()

        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, 300)

    def bootstrap(self):
        pygame.init()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == self.GAME_UPDATE and not (self.game.game_over):
                    self.game.moveDown()

                if event.type == pygame.KEYDOWN:
                    if self.game.game_over:
                        self.game.reset()

                    if event.key == pygame.K_LEFT and not (self.game.game_over):
                        self.game.moveLeft()

                    if event.key == pygame.K_RIGHT and not (self.game.game_over):
                        self.game.moveRight()

                    if event.key == pygame.K_DOWN and not (self.game.game_over):
                        self.game.moveDown()
                        self.game.updateScore(0, 1)

                    if event.key == pygame.K_UP and not (self.game.game_over):
                        self.game.rotate()

            self.screen.fill(Colors.dark_blue)

            score_value = self.title_font.render(
                str(self.game.score), True, Colors.white)
            self.screen.blit(score_value, score_value.get_rect(
                centerx=self.score_rect.centerx, centery=self.score_rect.centery))
            self.screen.blit(self.score_surface, (365, 20, 50, 50))
            self.screen.blit(self.next_surface, (375, 180, 50, 50))
            if self.game.game_over:
                self.screen.blit(self.game_over, (320, 450, 50, 50))
            # pygame.draw.rect(screen, Colors.ligth_blue, score_rect, 0, 10)
            # pygame.draw.rect(screen, Colors.ligth_blue, next_rect, 0, 10)

            self.game.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)
