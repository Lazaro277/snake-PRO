import sys

import pygame
from pygame import Surface, Rect, Font, K_ESCAPE, K_BACKSPACE

from game_code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED
from game_code.DBProxy import DBProxy
from game_code.Level import Level


class Set_goal:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level

    def run(self):

        pygame.mixer_music.load('./assets/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        name = ''
        digit_caractere = False

        while True:

            # load images
            bg_menu = pygame.image.load("./assets/background_objective.png").convert_alpha()
            bg_menu = pygame.transform.scale(bg_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
            bg_input_goal = pygame.image.load("./assets/bg_input_goal.jpg").convert_alpha()
            bg_input_goal = pygame.transform.scale(bg_input_goal, (200, 50))
            # draws background on screen
            self.screen.blit(bg_menu, (0, 0))
            self.screen.blit(bg_input_goal, (412, 378))


            self.set_goal_text(40, 'Now you must set a target score to', WHITE, ((SCREEN_WIDTH // 2), 90), 3)
            self.set_goal_text(40, 'achieve. After reaching the target,', WHITE, ((SCREEN_WIDTH // 2), 140), 3)
            self.set_goal_text(40, 'you can continue as long as you can.', WHITE, ((SCREEN_WIDTH // 2), 190), 3)
            self.set_goal_text(40, "If you don't reach the target, you lose.", WHITE, ((SCREEN_WIDTH // 2), 240), 3)
            self.set_goal_text(40, 'Enter your goal below.', WHITE, ((SCREEN_WIDTH // 2), 350), 3)
            self.set_goal_text(27, 'Press ENTER to continue', WHITE, ((SCREEN_WIDTH // 2), 500), 2)
            self.set_goal_text(27, 'Press ESC to exit', WHITE, ((SCREEN_WIDTH // 2), 550), 2)

            # Check events and close window\game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                    if event.key == K_BACKSPACE:
                        name = name[:-1]
                        if len(name) == 0:
                            digit_caractere = False
                    else:
                        if event.unicode.isdigit() and len(name) < 7:
                            name += event.unicode
                            digit_caractere = True
                    if digit_caractere:
                        if event.key == pygame.K_RETURN:
                            db_proxy = DBProxy('DBScore')
                            db_proxy.save_goal({'goal': name})
                            level = Level(self.screen)
                            level.run(self.level)

            self.set_goal_text(40, name, RED, ((SCREEN_WIDTH // 2), 400), 1)
            pygame.display.flip()

    def set_goal_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_weight: int):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # Renders the base text.
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # Creates an identical copy for the "faux bold" effect.
        shadow_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        # Desloca apenas 1 píxel para a direita
        shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + font_weight, text_center_pos[1]))

        # Draw both on the screen (the offset creates the intermediate weight)
        self.screen.blit(source=shadow_surf, dest=shadow_rect)
        self.screen.blit(source=text_surf, dest=text_rect)
