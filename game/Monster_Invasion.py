import sys  
import pygame

from Modules.settings import Settings
from Modules.Ship import Ship
from Modules.Alien import Alien

import Modules.game_function as gf

from pygame.sprite import Group

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Monster Invasion")

    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)        
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()