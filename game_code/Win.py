import sys

import pygame
from pygame import Font, Surface, Rect, K_ESCAPE

from game_code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, RED, WHITE, ORANGE, GREEN, OPTION_MENU_GAME_OVER_WIN
from game_code.DBProxy import DBProxy
from game_code.Score import Score


class Win:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        pygame.mixer_music.load('./assets/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        score = Score.show_round()
        score = str(score)
        db_proxy = DBProxy('DBScore')
        goal = db_proxy.show_goal()
        goal = str(goal)
        db_proxy.close()

        option_menu = 0

        while True:
            # load image
            bg_win = pygame.image.load("./assets/bg_menu.png").convert_alpha()
            bg_win = pygame.transform.scale(bg_win, (SCREEN_WIDTH, SCREEN_HEIGHT))
            #draws background on screen
            self.screen.blit(bg_win, (0, 0))

            self.win_text(150, 'WIN', RED, ((SCREEN_WIDTH / 2), 130), 5)

            self.win_text(50, f'Goal: {goal}', WHITE, (250, 350), 1)
            self.win_text(50, f'Score: {score}', WHITE, (780, 350), 1)

            for i in range(len(OPTION_MENU_GAME_OVER_WIN)):
                if i == 0:
                    if i == option_menu:
                        self.win_text(40, OPTION_MENU_GAME_OVER_WIN[i], WHITE, (330, 500), 1)
                    else:
                        self.win_text(40, OPTION_MENU_GAME_OVER_WIN[i], GREEN, (330, 500), 1)
                if i == 1:
                    if i == option_menu:
                        self.win_text(40, OPTION_MENU_GAME_OVER_WIN[i], WHITE, (670, 500), 1)
                    else:
                        self.win_text(40, OPTION_MENU_GAME_OVER_WIN[i], GREEN, (670, 500), 1)


            pygame.display.flip()

            # Check events and close window\game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RIGHT:
                        if option_menu < len(OPTION_MENU_GAME_OVER_WIN) - 1:
                            option_menu += 1
                        else:
                            option_menu = 0
                    if event.key == pygame.K_LEFT:
                        if option_menu > 0:
                            option_menu -= 1
                        else:
                            option_menu = len(OPTION_MENU_GAME_OVER_WIN) - 1
                    if event.key == pygame.K_RETURN:
                        return OPTION_MENU_GAME_OVER_WIN[option_menu]


    def win_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_weight: int):
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
