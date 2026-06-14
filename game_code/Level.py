import random
import sys

import pygame

from game_code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from game_code.Game_Over import Game_Over
from game_code.Score import Score


class Level:
    def __init__(self, screen):
        self.screen = screen

    def run(self, level:int):
        if level == 1:
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
        elif level == 2:
            # load music
            pygame.mixer_music.load('./assets/sound_level_2.aiff')
            # load image
            bg_menu = pygame.image.load("./assets/bg_level_2.png").convert_alpha()
            # load snake
            snake = pygame.image.load("./assets/snake_yellow.png").convert_alpha()
            # load body snake
            snake_body_img = pygame.image.load("./assets/snake_body_yellow.png").convert_alpha()
            # speed snake
            SPEED_SNAKE = 70

        apple = pygame.image.load('./assets/apple.png').convert_alpha()
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer_music.play(-1)

        bg_menu = pygame.transform.scale(bg_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
        snake_rect = snake.get_rect(left=(SCREEN_WIDTH / 2), top=(SCREEN_HEIGHT / 2))
        apple_rect = apple.get_rect()

        def spawn_apple():
            # Max safe position is screen size minus asset size
            max_x = SCREEN_WIDTH - apple_rect.width
            max_y = SCREEN_HEIGHT - apple_rect.height

            # Pick a random coordinate
            apple_rect.x = random.randint(0, max_x)
            apple_rect.y = random.randint(0, max_y)

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

                    # Set continuous direction based on key pressed
                    if event.key == pygame.K_UP:
                        direction_x = 0
                        direction_y = -32
                    elif event.key == pygame.K_DOWN:
                        direction_x = 0
                        direction_y = 32
                    elif event.key == pygame.K_LEFT:
                        direction_x = -32
                        direction_y = 0
                    elif event.key == pygame.K_RIGHT:
                        direction_x = 32
                        direction_y = 0

                if event.type == SNAKE_MOVE_EVENT:
                    # Update the head's position based on direction
                    snake_rect.x += direction_x
                    snake_rect.y += direction_y

                    snake_body.insert(0, snake_rect.copy())

                    # COLLISION DETECTION (If snake eats the apple)
                    if snake_rect.colliderect(apple_rect):
                        score = 10
                        score_round += score
                        Score.save(score, score_round)
                        spawn_apple()  # Move apple to a new random location
                    else:
                        snake_body.pop()

            # Screen boundaries constraints (Prevent snake from leaving the screen)
            if snake_rect.left < 0 or snake_rect.right > SCREEN_WIDTH or snake_rect.top < 0 or snake_rect.bottom > SCREEN_HEIGHT:
                game_over = Game_Over(self.screen)
                game_over.run()

            # 4. Rendering elements on the screen
            self.screen.blit(bg_menu, (0, 0))
            self.screen.blit(apple, apple_rect)
            # Draw the head using the main snake image
            self.screen.blit(snake, snake_body[0])
            # Draw the rest of the body using the body image
            for segment in snake_body[1:]:
                self.screen.blit(snake_body_img, segment)
            pygame.display.flip()