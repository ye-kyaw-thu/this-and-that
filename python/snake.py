## Written by Ye Kyaw Thu, LU Lab., Myanmar
## Old snake game
## Date: 14 Dec 2023

## Links of pictures
## for the github, check under fig/snake_game/
## Background:
## https://unsplash.com/
## Snake head:
## https://www.flaticon.com/search?word=snake%20head
## For foods:
## https://pixabay.com/

eat and game-over sound files (Game Over Arcade):
https://freesound.org/
import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 40
snake_speed = 5

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load images and sounds
#bg = pygame.image.load('background.jpg')

# Load and resize the background image
bg_original = pygame.image.load('background.jpg')
bg = pygame.transform.scale(bg_original, (dis_width, dis_height))


snake_head_img = pygame.image.load('snake_head.png')
snake_head_img = pygame.transform.scale(snake_head_img, (snake_block, snake_block))

food_img = pygame.image.load('food.png').convert()
food_img.set_colorkey(white)
food_img = pygame.transform.scale(food_img, (snake_block, snake_block))

eat_sound = pygame.mixer.Sound('eat_sound.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

# Direction of the snake
direction = "LEFT"

def score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    head = snake_head_img
    if direction == "RIGHT":
        head = pygame.transform.flip(snake_head_img, True, False)  # Flip horizontally
    elif direction == "LEFT":
        head = snake_head_img  # Original image is facing left, no change needed
    elif direction == "UP":
        head = pygame.transform.rotate(snake_head_img, 270)  # Rotate 90 degrees clockwise
    elif direction == "DOWN":
        head = pygame.transform.rotate(snake_head_img, 90)   # Rotate 90 degrees counterclockwise

    dis.blit(head, (snake_list[-1][0], snake_list[-1][1]))
    for x in snake_list[:-1]:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    global direction 

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    direction = "DOWN"

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over_sound.play()
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(bg, (0, 0))
        dis.blit(food_img, (foodx, foody))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over_sound.play()
                game_close = True

        our_snake(snake_block, snake_List)
        score(Length_of_snake - 1)

        pygame.display.update()

        if abs(x1 - foodx) < snake_block and abs(y1 - foody) < snake_block:
            eat_sound.play()
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            print(f"New food position: ({foodx}, {foody})")  # Debugging line

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
