'''
Ejercicio 5: Polígonos (triángulos y estrellas)
Objetivo: aprender a usar listas de puntos. - Dibuja un triángulo equilátero. - Dibuja una
estrella de 5 puntas. - Guarda la imagen como e5_poligonos.png.
'''
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((700,600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    lado = 200
    altura = (math.sqrt(3) * lado) / 2


    triangulo_puntos = [(350, 350 - altura), (250, 350), (450, 350)]
    pygame.draw.polygon(screen, "blue", triangulo_puntos)

    estrella_puntos = [
        (350, 420),  # punta superior
        (370, 470),
        (425, 470),
        (380, 500),
        (400, 550),
        (350, 520),
        (300, 550),
        (320, 500),
        (275, 470),
        (330, 470),
    ]
    pygame.draw.polygon(screen, "yellow", estrella_puntos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()