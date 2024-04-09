import pygame
import sys

pygame.init()

window_width, window_height = 500, 500
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_radius = 25
ball_x, ball_y = window_width // 2, window_height // 2
ball_speed = 20


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y = max(ball_y - ball_speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_y = min(ball_y + ball_speed, window_height - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_x = max(ball_x - ball_speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_x = min(ball_x + ball_speed, window_width - ball_radius)

   
    screen.fill(WHITE)

    
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    
    pygame.display.flip()

    
    pygame.time.Clock().tick(30)
