import pygame   #pip install pygame

pygame.init()   #inicializa los modulos de pygame

screen = pygame.display.set_mode((600,600))   #creamos la ventana

clock = pygame.time.Clock()    #reloj

running = True
COLOR = (20,50,190)
while running:

    for event in pygame.event.get():       #Deteccion del evento de cierre de ventana (X)
        if event.type == pygame.QUIT:
            running = False
            
        '''EVENTOS DEL MOUSE'''
        if event.type == pygame.MOUSEBUTTONDOWN: #Deteccion del evento de click del mouse
            print("Click en:", event.pos, "Boton:", event.button) #posicion del click
            pygame.draw.polygon(screen, "orange", [(400, 250), (450, 200), (500, 250), (475, 300), (425, 300)], width=5)
        if event.type == pygame.MOUSEBUTTONUP: #Deteccion del evento de soltar el click del mouse
            print("Soltaste en:", event.pos, "Boton:", event.button)
        if event.type == pygame.MOUSEMOTION: #Deteccion del evento de movimiento del mouse
            print("Moviendo en:", event.pos)
            
        '''EVENTOS DEL TECLADO'''
        if event.type == pygame.KEYDOWN:
            print("Tecla presionada:", event.key)
        if event.type == pygame.KEYUP:
            print("Tecla liberada:", event.key)
        
        '''Cambiar color con teclado'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:   #Tecla R
                COLOR = (255,0,0)         #Rojo
            elif event.key == pygame.K_g:   #Tecla G
                COLOR = (0,255,0)         #Verde
            elif event.key == pygame.K_b:   #Tecla B
                COLOR = (0,0,255)         #Azul
            elif event.key == pygame.K_y:   #Tecla Y
                COLOR = (255,255,0)       #Amarillo
            elif event.key == pygame.K_c:   #Tecla C
                COLOR = (0,255,255)       #Cyan
            elif event.key == pygame.K_m:   #Tecla M
                COLOR = (255,0,255)       #Magenta
            elif event.key == pygame.K_w:   #Tecla W
                COLOR = (255,255,255)     #Blanco
            elif event.key == pygame.K_k:   #Tecla K
                COLOR = (0,0,0)           #Negro
            else:
                screen.fill((200,200,200))     #Pintar la ventana de gris

        '''Dibujar un ciriculo en la posicion del mouse'''
        if event.type == pygame.MOUSEMOTION:
            if event.buttons == 1:
                pygame.draw.circle(screen, COLOR, event.pos, 10)  #Dibujar un circulo en la posicion del mouse

        screen.fill((200,200,200))     #Pintar la ventana de gris
    pygame.display.flip()  #actulizar la pantalla
    dt = clock.tick(60)


pygame.quit()   #cerrar