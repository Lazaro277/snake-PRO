import sys

import pygame
from pygame import Surface, Rect, Font, K_ESCAPE

from game_code.Set_goal import Set_goal
from game_code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE


class Objective_game:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level

    def run(self):

        pygame.mixer_music.load('./assets/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            # load image
            bg_menu = pygame.image.load("./assets/background_objective.png").convert_alpha()
            bg_menu = pygame.transform.scale(bg_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
            # draws background on screen
            self.screen.blit(bg_menu, (0, 0))


            self.objective_text(40, 'The goal of the game is to eat the ', WHITE, ((SCREEN_WIDTH // 2), 90), 3)
            self.objective_text(40, 'apple without hitting the edges or', WHITE, ((SCREEN_WIDTH // 2), 140), 3)
            self.objective_text(40, 'obstacles (level 2). With each apple', WHITE, ((SCREEN_WIDTH // 2), 190), 3)
            self.objective_text(40, 'eaten, the snake grows in size and', WHITE, ((SCREEN_WIDTH // 2), 240), 3)
            self.objective_text(40, 'the game becomes more difficult.', WHITE, ((SCREEN_WIDTH // 2), 290), 3)
            self.objective_text(40, 'Use the arrow keys to control the snake.', WHITE, ((SCREEN_WIDTH // 2), 370), 3)
            self.objective_text(27, 'Press ENTER to continue', WHITE, ((SCREEN_WIDTH // 2), 500), 2)
            self.objective_text(27, 'Press ESC to exit', WHITE, ((SCREEN_WIDTH // 2), 550), 2)
            pygame.display.flip()

            # Check events and close window\game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                    if event.key == pygame.K_RETURN:
                        set_goal = Set_goal(self.screen, self.level)
                        set_goal.run()

    def objective_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_weight: int):
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
