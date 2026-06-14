import sys

import pygame

from game_code.Level import Level
from game_code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, OPTION_MENU
from game_code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        # Game window size
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake PRO - by Lázaro Messias")

    def run(self):
        while True:
            menu = Menu(self.screen)
            return_menu = menu.run()

            if return_menu == OPTION_MENU[0]:
                # level 1
                level = Level(self.screen)
                level.run(1)

            elif return_menu == OPTION_MENU[1]:
                # level 2
                level = Level(self.screen)
                level.run(2)

            elif return_menu == OPTION_MENU[2]:
                # score
                pass

            elif return_menu == OPTION_MENU[3]:
                # exit
                pygame.quit()
                sys.exit()
            else:
                pygame.quit()
                sys.exit()