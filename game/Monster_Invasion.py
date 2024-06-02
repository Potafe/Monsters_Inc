import sys
import pygame

import Modules.settings as Settings

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Monster Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()




run_game()