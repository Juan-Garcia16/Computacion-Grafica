'''
Ejercicio 6: Composición (casa)
Objetivo: combinar varias formas. - Dibuja una casa con rectángulo (cuerpo), triángulo
(techo), puerta y ventana. - Añade un sol (circulo) y un jardín (rectángulo verde). - Guarda
la imagen como e6_casa.png.
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

    # cuerpo de la casa
    pygame.draw.rect(screen, "brown", (250,300,200,200))
    # techo
    pygame.draw.polygon(screen, "red", [(240,300),(460,300),(350,200)])
    # puerta
    pygame.draw.rect(screen, "gray", (320,400,60,100))
    # ventanas
    pygame.draw.rect(screen, "blue", (270,350,50,50))
    pygame.draw.rect(screen, "blue", (380,350,50,50))
    # jardin
    pygame.draw.rect(screen, "green", (0,500,700,100))
    # sol
    pygame.draw.circle(screen, "yellow", (600,100), 50)

    pygame.display.flip()
    clock.tick(60)

pygame.image.save(screen, "e6_casa.png")
pygame.quit()