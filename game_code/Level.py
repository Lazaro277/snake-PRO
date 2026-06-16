import random
import sys

import pygame
from pygame import Surface, Rect, Font
from game_code.Const import SCREEN_WIDTH, SCREEN_HEIGHT, OPTION_MENU_GAME_OVER_WIN, RED
from game_code.DBProxy import DBProxy
from game_code.Game_Over import Game_Over
from game_code.Score import Score
from game_code.Win import Win


class Level:
    def __init__(self, screen):
        self.screen = screen

    def run(self, level_current:int):
        if level_current == 1:
            # load music
            pygame.mixer_music.load('./assets/sound_level_1.wav')
            # load image
            bg_menu = pygame.image.load("./assets/bg_level_1.jpg").convert_alpha()
            # load snake
            snake = pygame.image.load("./assets/snake_green.png").convert_alpha()
            # load body snake
            snake_body_img = pygame.image.load("./assets/snake_body_green.png").convert_alpha()
            # speed snake
            SPEED_SNAKE = 100
        elif level_current == 2:
            # load music
            pygame.mixer_music.load('./assets/sound_level_2.aiff')
            # load image
            bg_menu = pygame.image.load("./assets/bg_level_2.png").convert_alpha()
            # load snake
            snake = pygame.image.load("./assets/snake_yellow.png").convert_alpha()
            # load body snake
            snake_body_img = pygame.image.load("./assets/snake_body_yellow.png").convert_alpha()
            # load blocks
            block1 = pygame.image.load('./assets/wall_block_64_0.png').convert_alpha()
            block2 = pygame.image.load('./assets/wall_block_64_1.png').convert_alpha()
            block3 = pygame.image.load('./assets/wall_block_64_2.png').convert_alpha()
            block4 = pygame.image.load('./assets/wall_block_64_3.png').convert_alpha()
            block5 = pygame.image.load('./assets/wall_block_64_4.png').convert_alpha()
            block6 = pygame.image.load('./assets/wall_block_64_6.png').convert_alpha()
            # speed snake
            SPEED_SNAKE = 70

        background_score = pygame.image.load('./assets/background_score.jpg').convert_alpha()
        background_score = pygame.transform.scale(background_score, (160, 64))
        bg_message_goal = pygame.image.load('./assets/bg_message_goal.png').convert_alpha()
        bg_message_goal = pygame.transform.scale(bg_message_goal, (202, 36))
        apple = pygame.image.load('./assets/apple.png').convert_alpha()
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1)

        bg_menu = pygame.transform.scale(bg_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
        start_x = ((SCREEN_WIDTH // 2) // 32) * 32
        start_y = ((SCREEN_HEIGHT // 2) // 32) * 32
        snake_rect = snake.get_rect(left=start_x, top=start_y)
        apple_rect = apple.get_rect()
        score_rect = pygame.Rect(0, 0, 160, 64)
        block1_rect = pygame.Rect(704, 512, 64, 64)
        block2_rect = pygame.Rect(704, 96, 64, 64)
        block3_rect = pygame.Rect(768, 96, 64, 64)
        block4_rect = pygame.Rect(832, 96, 64, 64)
        block5_rect = pygame.Rect(96, 512, 64, 64)
        block6_rect = pygame.Rect(96, 576, 64, 64)
        block7_rect = pygame.Rect(192, 192, 64, 64)

        def spawn_apple():
            # Grid columns (ex: 768 / 32 = 24 columns, indices 0 to 23)
            max_cols = SCREEN_WIDTH // 32
            max_rows = SCREEN_HEIGHT // 32

            while True:
                # Pick a random grid tile, then multiply by 32 to get pixel position
                apple_rect.x = random.randint(0, max_cols - 1) * 32
                apple_rect.y = random.randint(0, max_rows - 1) * 32

                if not apple_rect.colliderect(score_rect):
                    break

        # Spawn the first apple
        spawn_apple()

        # DIRECTION VARIABLES (The snake starts stationary)
        direction_x = 0
        direction_y = 0

        # Control the game's frame rate (FPS)
        clock = pygame.time.Clock()
        score_round = 0

        # Create a list to hold all body parts (rectangles or coordinates)
        # At the start, it only contains the head position
        snake_body = [snake_rect.copy()]

        # Define a unique ID for our custom event
        SNAKE_MOVE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(SNAKE_MOVE_EVENT, SPEED_SNAKE)

        Score.save(0, 0)

        goal_time = 0

        while True:
            # Maintain the game running at 60 frames per second
            clock.tick(60)

            # 2. Event Handling (Update direction state)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    # Set continuous direction based on key pressed (Blocking opposite directions)
                    if event.key == pygame.K_UP and direction_y <= 0:
                        direction_x = 0
                        direction_y = -32
                    elif event.key == pygame.K_DOWN and direction_y >= 0:
                        direction_x = 0
                        direction_y = 32
                    elif event.key == pygame.K_LEFT and direction_x <= 0:
                        direction_x = -32
                        direction_y = 0
                    elif event.key == pygame.K_RIGHT and direction_x >= 0:
                        direction_x = 32
                        direction_y = 0

                if event.type == SNAKE_MOVE_EVENT:
                    # Update the head's position based on direction
                    if direction_x != 0 or direction_y != 0:
                        snake_rect.x += direction_x
                        snake_rect.y += direction_y

                        snake_body.insert(0, snake_rect.copy())

                        # Screen boundaries constraints (Prevent snake from leaving the screen)
                        if snake_rect.left < 0 or snake_rect.right > SCREEN_WIDTH or snake_rect.top < 0 or snake_rect.bottom > SCREEN_HEIGHT:
                            self.verifies_victory(level_current)

                        # CHECK SELF-COLLISION (Lose when hitting her own body)
                        for segment in snake_body[1:]:
                            if snake_rect.colliderect(segment):
                                self.verifies_victory(level_current)

                        # CHECK COLLISION WITH SCORE BOX (Game Over if snake hits the score board)
                        if snake_rect.colliderect(score_rect):
                            self.verifies_victory(level_current)

                        # Check collision with block if level 2
                        if level_current == 2:
                            if snake_rect.colliderect(block1_rect) or snake_rect.colliderect(block2_rect) or snake_rect.colliderect(block3_rect) or snake_rect.colliderect(block4_rect) or snake_rect.colliderect(block5_rect) or snake_rect.colliderect(block6_rect) or snake_rect.colliderect(block7_rect):
                                self.verifies_victory(level_current)

                        # COLLISION DETECTION (If snake eats the apple)
                        if snake_rect.colliderect(apple_rect):
                            score = 10
                            score_round += score
                            Score.save(score, score_round)

                            db_proxy = DBProxy('DBScore')
                            goal = db_proxy.show_goal()
                            goal = int(goal)
                            db_proxy.close()
                            if score_round >= goal and goal_time == 0:
                                goal_time = pygame.time.get_ticks()

                            spawn_apple()  # Move apple to a new random location
                        else:
                            snake_body.pop()


            # 4. Rendering elements on the screen
            self.screen.blit(bg_menu, (0, 0))
            self.screen.blit(apple, apple_rect)
            # Draw the head using the main snake image
            self.screen.blit(snake, snake_body[0])
            # Draw the rest of the body using the body image
            for segment in snake_body[1:]:
                self.screen.blit(snake_body_img, segment)

            self.screen.blit(background_score, (0, 0))

            score = Score.show_round()
            score = str(score)
            db_proxy = DBProxy('DBScore')
            goal = db_proxy.show_goal()
            goal = str(goal)
            db_proxy.close()
            self.level_text(24, f'Meta: {goal}', RED, (70, 20), 0)
            self.level_text(24, f'Score: {score}', RED, (75, 45), 0)

            # Draw blocks level 2
            if level_current == 2:
                self.screen.blit(block1, block1_rect)
                self.screen.blit(block2, block2_rect)
                self.screen.blit(block3, block3_rect)
                self.screen.blit(block4, block4_rect)
                self.screen.blit(block5, block5_rect)
                self.screen.blit(block6, block6_rect)
                self.screen.blit(block1, block7_rect)

            if goal_time > 0:
                current_time = pygame.time.get_ticks()

                # If less than 5000 milliseconds (5 seconds) have passed, draw the text
                if current_time - goal_time < 3000:
                    self.screen.blit(bg_message_goal, (410, 13))
                    self.level_text(20, 'Goal achieved', RED, ((SCREEN_WIDTH / 2), 30), 2)

            pygame.display.flip()

    def call_game_over(self, level_current):
        from game_code.Game import Game

        game_over = Game_Over(self.screen)
        return_game_over = game_over.run()
        if return_game_over == OPTION_MENU_GAME_OVER_WIN[0]:
            # restart level 1
            level = Level(self.screen)
            level.run(level_current)
            return
        elif return_game_over == OPTION_MENU_GAME_OVER_WIN[1]:
            # return menu
            game = Game()
            game.run()
            return

    def call_win(self, level_current):
        from game_code.Game import Game

        win = Win(self.screen)
        return_win = win.run()
        if return_win == OPTION_MENU_GAME_OVER_WIN[0]:
            # restart level 1
            level = Level(self.screen)
            level.run(level_current)
            return
        elif return_win == OPTION_MENU_GAME_OVER_WIN[1]:
            # return menu
            game = Game()
            game.run()
            return

    def verifies_victory(self, level_current):
        score = Score.show_round()
        score = int(score)
        db_proxy = DBProxy('DBScore')
        goal = db_proxy.show_goal()
        goal = int(goal)
        db_proxy.close()

        if score >= goal:
            self.call_win(level_current)
        else:
            self.call_game_over(level_current)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_weight: int):
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