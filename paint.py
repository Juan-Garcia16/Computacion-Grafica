import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

drawing = False  # ¿Está el mouse presionado?
last_pos = None  # Última posición del mouse
color = (0, 0, 0)  # Color negro
grosor = 5

screen.fill((255, 255, 255))  # Fondo blanco

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Cuando presionas el mouse, empieza a dibujar
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        # Cuando sueltas el mouse, deja de dibujar
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Cuando mueves el mouse y estás dibujando
        if event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.line(screen, color, last_pos, event.pos, grosor)
            last_pos = event.pos
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill("white")
            elif event.key in [pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS]: #para asegurar que funcione en todos los teclados
                grosor += 3
            elif event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                grosor -= 10

    pygame.display.flip()
    clock.tick(60)

pygame.quit()