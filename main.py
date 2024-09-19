import pygame
import sys


pygame.init()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong Game')


# Pong ball
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


# Paddle 1
paddleL = pygame.Rect(20, 0, 10, 100)
paddleL.topleft = (50, SCREEN_HEIGHT/2 - 50)


# Paddle 2
paddleR = pygame.Rect(20, 0, 10, 100)
paddleR.topright = (1230, SCREEN_HEIGHT/2 - 50)

ball_speed_x = 6
ball_speed_y = 6


font = pygame.font.SysFont('Comic Sans MS', 42)

scoreR = 0
scoreL = 0

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleL.y -= 6
    if keys[pygame.K_s]:
        paddleL.y += 6
    if keys[pygame.K_UP]:
        paddleR.y -= 6
    if keys[pygame.K_DOWN]:
        paddleR.y += 6


    # Move the pong ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    
    # Check the Edges of the paddels
    #Left
    if paddleL.top <= 0:
        paddleL.top = 0
    if paddleL.bottom >= SCREEN_HEIGHT:
        paddleL.bottom = SCREEN_HEIGHT
    # Right
    if paddleR.top <= 0:
        paddleR.top = 0
    if paddleR.bottom >= SCREEN_HEIGHT:
        paddleR.bottom = SCREEN_HEIGHT


    # Check the Edges of the ball
    if ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0:
        scoreR += 1
        ball.x = SCREEN_WIDTH/2
    if ball.right >= SCREEN_WIDTH:
        scoreL += 1
        ball.x = SCREEN_WIDTH/2


    # Check for collisions
    if ball.colliderect(paddleL):
        ball_speed_x = -ball_speed_x
        ball_speed_y += 0.5
    if ball.colliderect(paddleR):
        ball_speed_x = -ball_speed_x
        ball_speed_y += 0.5


    screen.fill(BLACK)

    # Draw The Score
    scoreTextL = font.render(f'{scoreL}', True, WHITE)
    scoreTextR = font.render(f'{scoreR}', True, WHITE)
    screen.blit(scoreTextL, (20, 10))
    screen.blit(scoreTextR, (1240, 10))

    # Draw the pong ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw the Paddels
    pygame.draw.rect(screen, WHITE, paddleL)
    pygame.draw.rect(screen, WHITE, paddleR)

    # Draw the middle net
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    pygame.display.update()

    clock.tick(FPS)
