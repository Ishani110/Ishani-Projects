import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hungry Snake")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake attributes
snake_block_size = 20
snake_speed = 5
snake_body = []
snake_length = 1

# Food attributes
food_block_size = 20
food_x = random.randrange(0, SCREEN_WIDTH - food_block_size, food_block_size)
food_y = random.randrange(0, SCREEN_HEIGHT - food_block_size, food_block_size)

# Font
font = pygame.font.SysFont(None, 30)


# Function to display message
def message(msg, color):
    screen_text = font.render(msg, True, color)
    SCREEN.blit(screen_text, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


# Function to draw snake
def draw_snake(snake_block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(SCREEN, GREEN, [block[0], block[1], snake_block_size, snake_block_size])


# Main game loop
def game_loop():
    global snake_length  # Declaring snake_length as a global variable

    game_over = False
    game_close = False
    direction = "RIGHT"

    snake_x = SCREEN_WIDTH / 2
    snake_y = SCREEN_HEIGHT / 2

    snake_speed_x = 0
    snake_speed_y = 0

    global food_x
    global food_y

    CLOCK = pygame.time.Clock()  # Define CLOCK object

    while not game_over:
        while game_close:
            SCREEN.fill(WHITE)
            message("Game Over! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                    snake_speed_x = -snake_block_size
                    snake_speed_y = 0
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                    snake_speed_x = snake_block_size
                    snake_speed_y = 0
                elif event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                    snake_speed_y = -snake_block_size
                    snake_speed_x = 0
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                    snake_speed_y = snake_block_size
                    snake_speed_x = 0

        if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
            game_close = True

        snake_x += snake_speed_x
        snake_y += snake_speed_y

        SCREEN.fill(WHITE)
        pygame.draw.rect(SCREEN, RED, [food_x, food_y, food_block_size, food_block_size])

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block_size, snake_body)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = random.randrange(0, SCREEN_WIDTH - food_block_size, food_block_size)
            food_y = random.randrange(0, SCREEN_HEIGHT - food_block_size, food_block_size)
            snake_length += 1

        CLOCK.tick(snake_speed)  # Use CLOCK.tick() to control game speed

    pygame.quit()
    quit()


game_loop()
