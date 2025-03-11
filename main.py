# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
# from constants import *

def main():
    pygame.init();
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT));
    while( True ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return;
        pygame.Surface.fill( screen, (0,0,0) );
        pygame.display.flip();

    # print( "Starting Asteroids!" );
    # print( f"Screen width: {constants.SCREEN_WIDTH}");     
    # print( f"Screen height: {constants.SCREEN_HEIGHT}");


if __name__ == "__main__":
    main()

# source venv/bin/activate
