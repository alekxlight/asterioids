
import pygame
import constants
from circleshape import CircleShape
import shots


class Player( CircleShape ):
    def __init__(self, x, y):
        super().__init__( x,y, constants.PLAYER_RADIUS );
        self.rotation = 0;
        self.timer = 0;

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c];

    def draw(self, screen):
        points = self.triangle( );
        pygame.draw.polygon( screen, (255, 255, 255), points, width=2 );
        return;

    def rotate( self, dt ):
        self.rotation += constants.PLAYER_TURN_SPEED * dt;
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.rotate(dt);
        if keys[pygame.K_d]: self.rotate((-1)*dt);
        if keys[pygame.K_w]: self.move(dt);
        if keys[pygame.K_s]: self.move((-1)*dt);
        if keys[pygame.K_SPACE]: self.shoot( );
        self.timer -= dt;
        return;

    def move( self, dt ):
        forward = pygame.Vector2(0, 1).rotate(self.rotation);
        self.position += forward * constants.PLAYER_SPEED * dt;
        return;

    def shoot(self):
        if self.timer > 0: return;
        new_shot = shots.Shot( self.position.x, self.position.y );
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED;
        self.timer = constants.PLAYER_SHOOT_COOLDOWN;
        return;

