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
            pygame.draw.line(screen, "black", last_pos, event.pos, 5)
            last_pos = event.pos #actualiza la posición
            
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
            
            
            
            
        