import pygame

pygame.init()
ancho,alto = 500,500
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()
running = True
#igual que lo anterior hasta el momento

pos = [250,250]
pos_rect = [250,250]
dim_rect = [50,25]
radio = 15
vel = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed() #capturar las teclas pulsadas para guardarlas en keys
    
    #Mov Circulo
    if keys[pygame.K_UP]:
        pos[1] -= vel
    if keys[pygame.K_DOWN]:
        pos[1] += vel
    if keys[pygame.K_LEFT]:
        pos[0] -= vel
    if keys[pygame.K_RIGHT]:
        pos[0] += vel
    
    #Mov cuadro
    if keys[pygame.K_w]:
        pos_rect[1] -= vel
    if keys[pygame.K_s]:
        pos_rect[1] += vel
    if keys[pygame.K_a]:
        pos_rect[0] -= vel
    if keys[pygame.K_d]:
        pos_rect[0] += vel
        
    #Colision circulo con los bordes
    pos[0] = max(radio, min(ancho - radio, pos[0])) #limite X 
    pos[1] = max(radio, min(alto - radio, pos[1])) #limte Y
    
    #Conlision cuadro con los bordes
    pos_rect[0] = max(dim_rect[0] - dim_rect[0], min(ancho - dim_rect[0], pos_rect[0])) #limite X 
    pos_rect[1] = max(dim_rect[1] - dim_rect[1], min(alto - dim_rect[1], pos_rect[1])) #limte Y
    
    '''
    #Limite X
    if pos[0] - radio < 0: #izquieda
        pos[0] = radio
    if pos[0] + radio > ancho: #derecha
        pos[0] = ancho - radio
    #Limite Y
    if pos[1] - radio < 0: #arriba
        pos[1] = radio
    if pos[1] + radio > alto: #abajo
        pos[1] = alto - radio
    '''
    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, "red", pos, radio)
    pygame.draw.rect(screen, "blue", (pos_rect, dim_rect))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
