import sys

import pygame

from game_code.const import SCREEN_WIDTH, SCREEN_HEIGHT, OPTION_MENU
from game_code.menu import Menu


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
                pass

            elif return_menu == OPTION_MENU[1]:
                # level 2
                pass

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