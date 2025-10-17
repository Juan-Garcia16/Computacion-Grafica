'''
Ejercicio 3: Círculos concéntricos
Objetivo: entender el uso de círculos y radios. - Dibuja tres círculos concéntricos con
radios 60, 120 y 180. - Alterna entre relleno y borde. - Guarda la imagen como
e3_circulos.png.
'''
import pygame

pygame.init()
screen = pygame.display.set_mode((700,600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    pygame.draw.circle(screen, "red", (350,300), 60)
    pygame.draw.circle(screen, "blue", (350,300), 120, width=5)
    pygame.draw.circle(screen, "green", (350,300), 180, width=15)

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()