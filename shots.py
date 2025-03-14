

import pygame
import circleshape
import constants


class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS);

    def draw( self, screen ):
        pygame.draw.circle( screen, color="white", center=self.position, radius=self.radius, width=2 );
        return;

    def update(self, dt):
        self.position += self.velocity * dt;
        return;


