import sys
import pygame

from Modules.settings import Settings
from Modules.Ship import Ship
import Modules.game_function as gf

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Monster Invasion")

    ship = Ship(ai_settings, screen)
    
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)




run_game()