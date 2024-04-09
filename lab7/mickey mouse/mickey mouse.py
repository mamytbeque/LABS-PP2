import pygame
import datetime
import os

pygame.init()
done = False

window_width = 500
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

# Get the directory of the Python script
script_dir = os.path.dirname(__file__)

bg = pygame.image.load(os.path.join(script_dir, 'img/bg.png'))
bg = pygame.transform.scale(bg, (window_width, window_height))
hand_second_img = pygame.image.load(os.path.join(script_dir, 'img/hand_second.png'))
hand_second_img = pygame.transform.scale(hand_second_img, (150, 400))
hand_minute_img = pygame.image.load(os.path.join(script_dir, 'img/hand_minute.png'))
hand_minute_img = pygame.transform.scale(hand_minute_img, (150, 300))
rect = bg.get_rect(center=(250, 250))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(bg, (0, 0))
    current_time = datetime.datetime.now()
    angle_second = -(current_time.second * 6)
    angle_minute = -(current_time.minute * 6)

    hand_minute = pygame.transform.rotate(hand_minute_img, angle_minute)
    hand_minute_rect = hand_minute.get_rect(center=rect.center)
    screen.blit(hand_minute, hand_minute_rect.topleft)
    
    hand_second = pygame.transform.rotate(hand_second_img, angle_second)
    hand_second_rect = hand_second.get_rect(center=rect.center)
    screen.blit(hand_second, hand_second_rect.topleft)

    pygame.display.flip()

pygame.quit()
