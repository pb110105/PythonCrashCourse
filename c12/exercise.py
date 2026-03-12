#12-1. Blue Sky
import sys
import pygame
class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (150,200,255)
        self.character_speed = 4.0
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect(). width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Blue Sky demo")
        self.character = Character(self)
    def run_game(self):
        while True:
            self.check_events()
            self.character.update()
            self._update_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.character.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.character.moving_left = False
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        pygame.display.flip()
#12-2. Game Character
class Character:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('12/images/Fire Titan.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.character_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.character_speed
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)
if __name__ == '__main__':
    ai = Game()
    ai.run_game()