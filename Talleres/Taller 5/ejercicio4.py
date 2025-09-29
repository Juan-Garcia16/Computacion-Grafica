'''Ejercicio 4: Dibujo Libre (Pincel)
Crea un programa donde el usuario pueda dibujar a mano alzada manteniendo presionado el
click izquierdo del mouse:
- Mantener presionado el click izquierdo → Dibuja una línea continua siguiendo el
movimiento.
- Soltar el mouse → Detiene el dibujo.
- Tecla C → Limpia la pantalla.
- Teclas + y - → Aumentan o disminuyen el grosor del pincel.'''
import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True
drawing = False
last_pos = None
grosor = 5
screen.fill("white")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
            
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            
        if event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.line(screen, "black", last_pos, event.pos, grosor)
            last_pos = event.pos #actualiza la posicion
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill("white")
            elif event.key in [pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS]:
                grosor += 1
            elif event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                grosor -= 1
            
    pygame.display.flip()
    clock.tick(90)
    
pygame.quit()
            
            
            
            
        