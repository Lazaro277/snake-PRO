import sys

import pygame
from pygame import Font, Surface, Rect, K_ESCAPE

from game_code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, RED, WHITE, ORANGE
from game_code.Score import Score


class Game_Over:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        option_menu = 0
        pygame.mixer_music.load('./assets/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        score = Score.show_round()
        score = str(score)

        while True:

            # load image
            bg_game_over = pygame.image.load("./assets/bg_menu.png").convert_alpha()
            bg_game_over = pygame.transform.scale(bg_game_over, (SCREEN_WIDTH, SCREEN_HEIGHT))
            #draws background on screen
            self.screen.blit(bg_game_over, (0, 0))

            self.game_over_text(150, 'GAME', RED, ((SCREEN_WIDTH / 2), 70), 3)
            self.game_over_text(150, 'OVER', RED, ((SCREEN_WIDTH / 2), 190), 5)

            self.game_over_text(50, 'SCORE', WHITE, ((SCREEN_WIDTH // 2), 350), 1)
            self.game_over_text(70, score, ORANGE, ((SCREEN_WIDTH // 2), 430), 2)
            Score.save(0, 0)


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


    def game_over_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_weight: int):
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
