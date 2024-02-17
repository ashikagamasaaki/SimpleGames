import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 400))
    pygame.display.set_caption("Simple Pygame")
    
    while(1):
        screen.fill((0, 0, 0))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



if __name__ == '__main__':
    main()
