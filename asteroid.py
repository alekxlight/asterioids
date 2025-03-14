
import random
import pygame
import circleshape
import constants


class Asteroid( circleshape.CircleShape ):
    def __init__(self, x, y, radius):
        super().__init__( x,y, radius );
        self.rotation = 0;

    def draw( self, screen ):
        pygame.draw.circle( screen, color=(255, 255, 255), center=self.position, radius=self.radius, width=2 );
        return;

    def update(self, dt):
        self.position += self.velocity * dt;
        return;

    def split(self):
        self.kill();
        if self.radius <= constants.ASTEROID_MIN_RADIUS: return;
        blue_angle = random.uniform( 20, 50 );
        ccw_vector = self.velocity.rotate( blue_angle );
        cw_vector  = self.velocity.rotate( (-1)*blue_angle );
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS;
        ccw_asteroid = Asteroid( self.position.x, self.position.y, new_radius );
        ccw_asteroid.velocity = ccw_vector * 1.2;
        cw_asteroid = Asteroid( self.position.x, self.position.y, new_radius );
        cw_asteroid.velocity = cw_vector * 1.2;
        return;


    