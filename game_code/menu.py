import sys

import pygame
from pygame import Font, Surface, Rect, K_ESCAPE

from game_code.const import SCREEN_WIDTH, SCREEN_HEIGHT, RED, ORANGE, OPTION_MENU, BLUE, GREEN, WHITE


class Menu:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        option_menu = 0
        pygame.mixer_music.load('./assets/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            # load image
            bg_menu = pygame.image.load("./assets/bg_menu.png").convert_alpha()
            bg_menu = pygame.transform.scale(bg_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
            #draws background on screen
            self.screen.blit(bg_menu, (0, 0))

            self.menu_text(150, 'Snake', ORANGE, ((SCREEN_WIDTH / 2), 70), 3)
            self.menu_text(150, 'PRO', RED, ((SCREEN_WIDTH / 2), 190), 5)

            for i in range(4):
                if i == 0:
                    if i == option_menu:
                        self.menu_text(50, OPTION_MENU[i], WHITE, (300, 370), 1)
                    else:
                        self.menu_text(50, OPTION_MENU[i], GREEN, (300, 370), 1)
                if i == 1:
                    if i == option_menu:
                        self.menu_text(50, OPTION_MENU[i], WHITE, (700, 370), 1)
                    else:
                        self.menu_text(50, OPTION_MENU[i], GREEN, (700, 370), 1)
                if i == 2:
                    if i == option_menu:
                        self.menu_text(50, OPTION_MENU[i], WHITE, (300, 470), 1)
                    else:
                        self.menu_text(50, OPTION_MENU[i], GREEN, (300, 470), 1)
                if i == 3:
                    if i == option_menu:
                        self.menu_text(50, OPTION_MENU[i], WHITE, (700, 470), 1)
                    else:
                        self.menu_text(50, OPTION_MENU[i], GREEN, (700, 470), 1)
            pygame.display.flip()

            pygame.display.update()

            # Check events and close window\game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if option_menu < len(OPTION_MENU) - 1:
                            option_menu += 1
                        else:
                            option_menu = 0
                    if event.key == pygame.K_LEFT:
                        if option_menu > 0:
                            option_menu -= 1
                        else:
                            option_menu = len(OPTION_MENU) - 1
                    if event.key == pygame.K_RETURN:
                        return OPTION_MENU[option_menu]
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_weight: int):
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
