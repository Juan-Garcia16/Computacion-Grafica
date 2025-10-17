'''
Ejercicio 2: Rectángulos y bordes
Objetivo: practicar el dibujo de rectángulos. - Dibuja un rectángulo relleno centrado de
300×200. - Dibuja un marco (solo borde) alrededor del lienzo. - Guarda la imagen como
e2_rectangulos.png.
'''
import pygame
#200 a 500
pygame.init()  
screen = pygame.display.set_mode((700, 600))  
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    #rectangulos
    pygame.draw.rect(screen, "green", (200, 200, 300, 200))
    pygame.draw.rect(screen, "blue", (0,0,700,600), width=5)

    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()