import pygame
from time import time

targetFPS = 150
displayFPS = True
backgroundColour = (31, 32, 38)

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
pygame.display.set_caption("Denali LOGIC")
pygame.display.set_icon(pygame.image.load("denali.png"))
clock = pygame.time.Clock()
running = True

fpstimer = time()
fpscount = 0
fps = targetFPS
fpscountamount = 75

font = pygame.font.SysFont('Consolas', 15)

while running:
    fpscount += 1
    if fpscount == fpscountamount:
        fpscount = 0
        fps = 1/((time()-fpstimer)/fpscountamount)
        fpstimer = time()

    # COMPUTE
    for event in pygame.event.get():
        # End if window X is pressed
        if event.type == pygame.QUIT:
            running = False

    # RENDER

    screen.fill(backgroundColour)
    
    #FPS COUNT
    if displayFPS: screen.blit(font.render(f'FPS: {round(fps)}', False, (255, 255, 255)),(0,0))

    pygame.display.flip()

    clock.tick(targetFPS)

pygame.quit()
