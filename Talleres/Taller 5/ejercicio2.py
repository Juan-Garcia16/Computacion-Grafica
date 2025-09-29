'''Ejercicio 2: Eventos del Mouse
Crea un programa que al hacer clic en la ventana se dibujen diferentes formas:
- Click izquierdo → Dibuja un círculo azul en la posición del clic.
- Click derecho → Dibuja un cuadrado rojo en la posición del clic.
- Clic con la rueda (botón central) → Dibuja un triángulo verde en la posición del clic.'''
import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
screen.fill("white")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(screen, "blue", event.pos, 20)
            elif event.button == 2:
                pygame.draw.polygon(screen, "green", [(event.pos[0], event.pos[1]-20), (event.pos[0]-20, event.pos[1]+20), (event.pos[0]+20, event.pos[1]+20)])
            elif event.button == 3:
                pygame.draw.rect(screen, "red", (event.pos[0] - 25, event.pos[1] - 25, 50, 50))
                

    
    pygame.display.flip()
    dt = clock.tick(60)
    
pygame.quit()