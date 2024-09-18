import pygame

pygame.mixer.init()
pygame.mixer.music.load('pia.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar a música...  ')