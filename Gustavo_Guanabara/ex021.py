# Desafio #021
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Example de uso do pygame com game de aliens
# No terminal foi executado o comando: pip install pygame
# import pygame.examples.aliens as aliens
# aliens.main()

import pygame
pygame.init()
# pygame.mixer.init()
pygame.mixer.music.load('ex021.ogg')
pygame.mixer.music.play()
pygame.event.wait()
