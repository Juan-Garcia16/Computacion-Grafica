'''Ejercicio 3: Teclado + Mouse
Crea un programa que combine el uso del teclado y del mouse para generar un pequeño
'paint':
- Teclas R, G, B → Cambian el color actual de dibujo.
- Click izquierdo → Dibuja un círculo en la posición del clic, con el color actual.
- Click derecho → Dibuja un cuadrado en la posición del clic, con el color actual.
- Tecla C → Borra todo el lienzo (limpia la pantalla).
- Teclas + y - → Aumentan o disminuyen el tamaño de la figura a dibujar.'''
import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True
screen.fill("white")
color = (255, 255, 255)
tamanio = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255,0,0)
            elif event.key == pygame.K_g:
                color = (0,255,0)
            elif event.key == pygame.K_b:
                color = (0,0,255)
            elif event.key == pygame.K_c:
                screen.fill("white")
            elif event.key in [pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS]: #para asegurar que funcione en todos los teclados
                tamanio += 10
            elif event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                tamanio -= 10
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(screen, color, event.pos, tamanio)
            elif event.button == 3:
                pygame.draw.rect(screen, color, (event.pos[0] - tamanio/2, event.pos[1] - tamanio/2, tamanio, tamanio))
    
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
        