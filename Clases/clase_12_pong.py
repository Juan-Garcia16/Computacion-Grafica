import pygame

pygame.init()
ancho,alto = 500,500
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()
running = True
#igual que lo anterior hasta el momento

pos_cicle = [250,250]
pos_rect1 = [0,250]
pos_rect2 = [475,250]
dim_rect = [25,50]
radio = 15
vel = 8
vel_X = 12
vel_Y = 12
score1 = 0
score2 = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed() #capturar las teclas pulsadas para guardarlas en keys
    
    #Mov Circulo
    pos_cicle[0] += vel_X
    pos_cicle[1] += vel_Y
    
    #Mov jugador 1
    if keys[pygame.K_w]:
        pos_rect1[1] -= vel
    if keys[pygame.K_s]:
        pos_rect1[1] += vel

    #Mov jugador 2
    if keys[pygame.K_UP]:
        pos_rect2[1] -= vel
    if keys[pygame.K_DOWN]:
        pos_rect2[1] += vel
        
    
    #Conlision cuadro con los bordes
    pos_rect1[0] = max(0, min(ancho - dim_rect[0], pos_rect1[0])) #limite X
    pos_rect1[1] = max(0, min(alto - dim_rect[1], pos_rect1[1])) #limte Y
    
    pos_rect2[0] = max(0, min(ancho - dim_rect[0], pos_rect2[0])) #limite X
    pos_rect2[1] = max(0, min(alto - dim_rect[1], pos_rect2[1])) #limte Y


    #rebote superior
    if pos_cicle[1] - radio < 0:
        vel_Y *= -1

    #rebote inferior
    if pos_cicle[1] + radio > alto:
        vel_Y *= -1
        
    #rebote derecha
    if pos_cicle[0] > ancho:
        pos_cicle = [250,250]
        score1 += 1
        
    #rebote izquierda
    if pos_cicle[0] < 0:
        pos_cicle = [250,250]
        score2 += 1

    screen.fill((0,0,0))
    
    
    b = pygame.draw.circle(screen, "red", pos_cicle, radio)
    c1 = pygame.draw.rect(screen, "white", (pos_rect1, dim_rect))
    c2 = pygame.draw.rect(screen, "white", (pos_rect2, dim_rect))
    
    if b.colliderect(c1) or b.colliderect(c2):
        vel_X *= -1
    
    pygame.display.flip()
    clock.tick(90)

pygame.quit()
print("Score jugador 1:", score1)
print("Score jugador 2:", score2)