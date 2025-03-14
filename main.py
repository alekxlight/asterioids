

import sys
import pygame
# import constants
from constants import *
from player import Player
import asteroid
import asteroidfield
import shots

def main():
    pygame.init();
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
    game_clock = pygame.time.Clock();
    dt = 0;  ### delta time

    updatable = pygame.sprite.Group();
    drawable  = pygame.sprite.Group();
    Player.containers = (updatable, drawable);

    asteroids = pygame.sprite.Group();
    asteroid.Asteroid.containers = (asteroids, updatable, drawable);

    asteroidfield.AsteroidField.containers = updatable;
    afield = asteroidfield.AsteroidField( );

    all_shots = pygame.sprite.Group();
    shots.Shot.containers = (all_shots, updatable, drawable);  ### i would not have thought of this

    player = Player( SCREEN_WIDTH/2, SCREEN_HEIGHT/2 );

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return;
        pygame.Surface.fill( screen, (0,0,0) );
        # player.update(dt);
        for this_group in updatable: this_group.update( dt );
        for this_asteroid in asteroids:
            if this_asteroid.collision_detected( player ):
                print( "Game over!" );
                sys.exit();
            for this_shot in all_shots:
                if this_shot.collision_detected( this_asteroid ):
                    this_shot.kill();
                    this_asteroid.split();

        # player.draw(screen);
        for this_group in drawable:  this_group.draw( screen );
        for this_shot in all_shots: this_shot.draw( screen );
        pygame.display.flip();

        ### end
        dt = game_clock.tick( 60 ) / 1000;

    # print( "Starting Asteroids!" );
    # print( f"Screen width: {constants.SCREEN_WIDTH}");     
    # print( f"Screen height: {constants.SCREEN_HEIGHT}");


if __name__ == "__main__":
    main()

# source venv/bin/activate
