import pygame  # Importa la librería pygame para gráficos y juegos

pygame.init()  # Inicializa todos los módulos de pygame
screen = pygame.display.set_mode((600, 600))  # Crea una ventana de 600x600 píxeles
clock = pygame.time.Clock()  # Crea un reloj para controlar los FPS

running = True
while running:  # Bucle principal del programa
    for event in pygame.event.get():  # Procesa los eventos de la ventana
        if event.type == pygame.QUIT:  # Si se cierra la ventana
            running = False  # Termina el bucle

    screen.fill("white")  # Rellena la ventana con color blanco

    # Dibuja una línea azul
    # screen: superficie donde se dibuja
    # "blue": color de la línea
    # (50,50): punto inicial (x, y)
    # (100,100): punto final (x, y)
    # 5: grosor de la línea
    pygame.draw.line(screen, "blue", (50,50), (100,100), 5)

    # Dibuja un círculo rojo
    # screen: superficie donde se dibuja
    # "red": color del círculo
    # (80,80): centro del círculo (x, y)
    # 30: radio
    # width=5: grosor del borde (si se omite, el círculo es sólido)
    pygame.draw.circle(screen, "red", (80,80), 30, width=5)

    # Dibuja un rectángulo verde
    # screen: superficie donde se dibuja
    # "green": color del rectángulo
    # (200,200,100,200): (x, y, ancho, alto)
    # width=5: grosor del borde
    pygame.draw.rect(screen, "green", (200,200,100,200), width=5)

    # Dibuja un polígono púrpura
    # screen: superficie donde se dibuja
    # "purple": color del polígono
    # [(300,300), (350,350), (400,300), (350,250)]: lista de vértices (x, y)
    # width=5: grosor del borde
    pygame.draw.polygon(screen, "purple", [(300,300), (400,300), (400,300), (350,200)], width=5)

    # Crea un pentágono
    pygame.draw.polygon(screen, "orange", [(400, 250), (450, 200), (500, 250), (475, 300), (425, 300)], width=5)
    
    # Dibuja una elipse cian
    # screen: superficie donde se dibuja
    # "cyan": color de la elipse
    # (100, 400, 200, 100): (x, y, ancho, alto) del rectángulo que contiene la elipse
    # width=5:grosor del borde
    pygame.draw.ellipse(screen, "cyan", (100, 400, 200, 100), width=5)  

    # Dibuja un arco magenta
    # screen: superficie donde se dibuja
    # "magenta": color del arco
    # (300, 400, 200, 100): (x, y, ancho, alto) del rectángulo que contiene el arco
    # 0: ángulo de inicio
    # 3.14: ángulo de fin
    # width=5: grosor del borde
    pygame.draw.arc(screen, "magenta", (300, 400, 200, 100), 0, 3.14, width=5)
    
    
    pygame.display.flip()  # Actualiza la pantalla con los nuevos dibujos
    dt = clock.tick(60)  # Limita el bucle a 60 FPS y devuelve el tiempo desde el último tick