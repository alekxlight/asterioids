# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import constants
from constants import *
from player import Player

def main():
    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
    game_clock = pygame.time.Clock();
    dt = 0;  ### delta time
    player = Player( SCREEN_WIDTH/2, SCREEN_HEIGHT/2 );
    while( True ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return;
        pygame.Surface.fill( screen, (0,0,0) );
        player.update(dt);
        player.draw(screen);
        pygame.display.flip();

        ### end
        dt = game_clock.tick( 60 ) / 1000;

    # print( "Starting Asteroids!" );
    # print( f"Screen width: {constants.SCREEN_WIDTH}");     
    # print( f"Screen height: {constants.SCREEN_HEIGHT}");


if __name__ == "__main__":
    main()

# source venv/bin/activate
