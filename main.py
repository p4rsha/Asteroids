import pygame
from constants import *
from logger import log_state, log_event 
from player import *
from asteroidfield import *
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: { pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    


    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()


    clock_object = pygame.time.Clock()
    dt = 0





    while True:
        log_state()

        for event in pygame.event.get():
               
               if event.type == pygame.QUIT:
                 return

        for object in updatable:
            object.update(dt)

        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for bullet in shots:
                if bullet.collides_with(object):
                    log_event("asteroid_shot")
                    bullet.kill()
                    object.split()

        


        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        

        dt = clock_object.tick(60) / 1000 
    
    

        
        

if __name__ == "__main__":
    main()
