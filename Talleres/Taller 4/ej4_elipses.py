'''
Ejercicio 4: Elipses y cara simple
Objetivo: trabajar con elipses. - Dibuja una elipse grande como cara. - Añade dos elipses
pequeñas como ojos. - Dibuja una elipse delgada como boca (solo borde). - Guarda la
imagen como e4_cara.png.
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

    pygame.draw.ellipse(screen, "red", (200,100,300,400))  # cara
    pygame.draw.ellipse(screen, "black", (270,250,50,30))  # ojo izquierdo
    pygame.draw.ellipse(screen, "black", (380,250,50,30))  # ojo derecho
    pygame.draw.ellipse(screen, "black", (300,350,100,40), width=5)  # boca

    pygame.display.flip()
    clock.tick(60)

pygame.quit()