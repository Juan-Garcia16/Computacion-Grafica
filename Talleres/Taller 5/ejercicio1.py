'''Ejercicio 1: Eventos de Teclado
Crea un programa que al presionar las siguientes teclas, el fondo cambie de color:
- Tecla R → Fondo rojo.
- Tecla G → Fondo verde.
- Tecla B → Fondo azul.
- Tecla Espacio → Fondo blanco.'''
import pygame

pygame.init()  # Inicializa Pygame
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
screen.fill("white")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill("red")
            elif event.key == pygame.K_g:
                screen.fill("green")
            elif event.key == pygame.K_b:
                screen.fill("blue")
            elif event.key == pygame.K_SPACE:
                screen.fill("white")

    pygame.display.flip()
    dt = clock.tick(60)
    
pygame.quit()
            
        
