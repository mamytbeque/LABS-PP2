import pygame
import os

pygame.init()
pygame.display.set_caption("music player")
screen = pygame.display.set_mode((360, 360))

music_directory = r"C:\Users\ualik\Desktop\studium\2 semester\Principles of Programming 2\music" #директория к папке
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")] #музыки

pygame.mixer.init()

def play_music():
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music(): #продолжить где остановился
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def play_next():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play_music()

def play_previous():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play_music()

current_track = 0
play_music()  

running = True
music_playing = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_playing:
                    pause_music()
                    music_playing = False
                else:
                    unpause_music()
                    music_playing = True
            elif event.key == pygame.K_RIGHT:
                play_next()
            elif event.key == pygame.K_LEFT:
                play_previous()

    screen.fill((0, 0, 0))

    font = pygame.font.SysFont(None, 24)
    text = font.render(f"{music_files[current_track]}", True, (0, 255, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
