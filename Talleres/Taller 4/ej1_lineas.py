'''
Ejercicio 1: Líneas y coordenadas
Objetivo: aprender a trazar líneas con distintos grosores. - Dibuja una cuadrícula con
cuadros de 100 píxeles. - Añade tres líneas de diferentes colores y grosores. - Guarda la
imagen como e1_lineas.png.
'''
import pygame

pygame.init()  
screen = pygame.display.set_mode((700, 600))  
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    #cuadricula
    for x in range(0, 701, 100):
        pygame.draw.line(screen, "gray", (x, 0), (x, 700), 1)
    for y in range(0, 701, 100):
        pygame.draw.line(screen, "gray", (0, y), (700, y), 1)
    
    #lineas
    pygame.draw.line(screen, "red", (0,200), (700,200), 15)
    pygame.draw.line(screen, "green", (0,300), (700,300), 10)
    pygame.draw.line(screen, "blue", (0,400), (700,400), 5)

    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()