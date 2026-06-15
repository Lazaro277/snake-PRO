import sys

import pygame

from game_code.Objective_game import Objective_game
from game_code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, OPTION_MENU
from game_code.Menu import Menu
from game_code.Score import Score


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
                objective = Objective_game(self.screen, 1)
                objective.run()

            elif return_menu == OPTION_MENU[1]:
                # level 2
                objective = Objective_game(self.screen, 2)
                objective.run()

            elif return_menu == OPTION_MENU[2]:
                # score
                score = Score(self.screen)
                score.show()

            elif return_menu == OPTION_MENU[3]:
                # exit
                pygame.quit()
                sys.exit()
            else:
                pygame.quit()
                sys.exit()