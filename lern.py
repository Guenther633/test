import pygame

import random

import time

pygame.init()

screen = pygame.display.set_mode((1000, 800))

clock = pygame.time.Clock()

random_pos = random.randint(0, 800), random.randint(0, 600)

player = pygame.Rect(100, 100, 50, 50)

#block = pygame.Rect(400, 250, 100, 100)

#block_2 = pygame.Rect(200, 250, 100, 100)

random_size = random.randint(50, 150)

counter = 0

block_3 = pygame.Rect(random_pos[0], random_pos[1], (random_size), (random_size))

block_destroyed = False

speed = 10

running = True
while running:
    screen.fill((0, 255, 0)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.x -= speed

    if keys[pygame.K_d]:
        player.x += speed

    if keys[pygame.K_w]:
        player.y -= speed

    if keys[pygame.K_s]:
        player.y += speed

    # Block 3 zerstören
    if player.colliderect(block_3):
        spawn_x = random.randint(0, 800)
        spawn_y = random.randint(0, 600)
        block_3.x = spawn_x
        block_3.y = spawn_y
        random_size = random.randint(50, 150)
        block_3.width = random_size
        block_3.height = random_size
        block_destroyed = True
        player.x = 500
        player.y = 400
        pygame.time.delay(100)
        counter += 1


    # Block 2 erst aktiv wenn Block 1 weg ist
    #if block_destroyed:
        #if player.colliderect(block_2):
         #   block_2.x = -1000
          #  pygame.time.delay(1000)
          #  running = False



    pygame.draw.rect(screen, (0, 0, 255), player)

    pygame.draw.rect(screen, (255, 0, 0), block_3)

    # Block 2 erst anzeigen wenn Block 1 weg ist
   # if block_destroyed:
    #    pygame.draw.rect(screen, (255, 0, 0), block_2)

    # Display the counter
    counter_surface = pygame.font.Font(None, 36).render(f"Score: {counter}", True, (0, 0, 0))
    counter_rect = counter_surface.get_rect(topleft=(10, 10))
    screen.blit(counter_surface, counter_rect)

    pygame.display.flip()

    clock.tick(60)

    if counter >=10:
        running = False 





pygame.quit()