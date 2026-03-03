#12-1. Blue Sky
import sys
import pygame
class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (150,200,255)
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Blue Sky demo")
        self.character = Character(self)
    def run_game(self):
        while True:
            self.check_events()
            self._update_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        pygame.display.flip()
#12-2. Game Character
class Character:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('12/images/Fire Titan.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)
if __name__ == '__main__':
    ai = Game()
    ai.run_game()