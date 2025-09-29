'''
Ejercicio 1: Líneas y coordenadas
Objetivo: aprender a trazar líneas con distintos grosores. - Dibuja una cuadrícula con
cuadros de 100 píxeles. - Añade tres líneas de diferentes colores y grosores. - Guarda la
imagen como e1_lineas.png.
'''
import pygame

pygame.init()  
screen = pygame.display.set_mode((700, 700))  
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    
    pygame.draw.line(screen, "red", (200,200), (500,200), 15)
    pygame.draw.line(screen, "green", (200,300), (500,300), 10)
    pygame.draw.line(screen, "blue", (200,400), (500,400), 10)
    
    pygame.draw.line(screen, "red", (200,200), (200,500), 15)
    pygame.draw.line(screen, "green", (300,200), (300,500), 10)
    pygame.draw.line(screen, "blue", (400,200), (400,500), 10)
    
    pygame.display.flip()
    dt = clock.tick(60)