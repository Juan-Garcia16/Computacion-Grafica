'''
Ejercicio 7: Banderas geométricas
Objetivo: practicar proporciones y alineación. - Dibuja dos banderas a elección entre: -
Colombia (franjas horizontales 50%-25%-25%). - Japón (círculo rojo centrado en fondo
blanco). - Francia (tres franjas verticales iguales). - Guarda la imagen como
e8_banderas.png.
'''
import pygame

pygame.init()
screen = pygame.display.set_mode((700,400))
clock = pygame.time.Clock()
fondo = (220, 220, 220)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(fondo)
    
    # bandera de Colombia
    pygame.draw.rect(screen, "yellow", (50,100,250,100))
    pygame.draw.rect(screen, "blue", (50,200,250,50))
    pygame.draw.rect(screen, "red", (50,250,250,50))
    
    # bandera de Japón
    pygame.draw.rect(screen, "white", (400,100,250,200))
    pygame.draw.circle(screen, "red", (525,200), 50)

    pygame.display.flip()
    clock.tick(60)

pygame.image.save(screen, "e7_banderas.png")
pygame.quit()