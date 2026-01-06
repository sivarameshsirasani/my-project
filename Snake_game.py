import pygame
import time
import random

# Initialise pygame
pygame.init()

# Screen Dimensions
WIDTH = 800
HEIGHT = 600
UNIT_SIZE = 20

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Setup Display
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game - Python Version')

# Clock for controlling speed
clock = pygame.time.Clock()
SNAKE_SPEED = 10 

# Font for Score and Game Over
font_style = pygame.font.SysFont("Arial", 25)
score_font = pygame.font.SysFont("Arial", 20)

def your_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    dis.blit(value, [10, 10])

def game_over_message(score):
    msg = font_style.render("Game Over", True, RED)
    score_msg = font_style.render("Score: " + str(score), True, WHITE)
    dis.blit(msg, [WIDTH / 2 - 60, HEIGHT / 2 - 20])
    dis.blit(score_msg, [WIDTH / 2 - 40, HEIGHT / 2 + 20])

def gameLoop():
    game_over = False
    game_close = False

    x1 = 100
    y1 = 100

    x1_change = UNIT_SIZE
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - UNIT_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - UNIT_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            dis.fill(BLACK)
            game_over_message(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -UNIT_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = UNIT_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -UNIT_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = UNIT_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(BLACK)
        pygame.draw.rect(dis, RED, [foodx, foody, UNIT_SIZE, UNIT_SIZE])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(dis, GREEN, [x[0], x[1], UNIT_SIZE, UNIT_SIZE])

        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - UNIT_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - UNIT_SIZE) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

gameLoop()