#!/usr/bin/env python3 # -- coding: utf-8 --

import pygame, pygame.locals 
# On initialise pygame 
pygame.init() 
taille_fenetre = (600, 400) 
fenetre_rect = pygame.Rect((0, 0), taille_fenetre) 
screen = pygame.display.set_mode(taille_fenetre)

BLEU_NUIT = ( 5, 5, 30) 
VERT = ( 0, 255, 0) 
JAUNE = (255, 255, 0)

timer = pygame.time.Clock()

joueur = pygame.Surface((25, 25)) 
joueur.fill(JAUNE) 
# Position du joueur 
x, y = 25, 100 
# Vitesse du joueur 
vx, vy = 0, 0 
# Gravité vers le bas donc positive 
GRAVITE = 2

mur = pygame.Surface((25, 25)) 
mur.fill(VERT)

niveau = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]

def dessiner_niveau(surface, niveau):
# """Dessine le niveau sur la surface donnée.Utilise la surface mur pour dessiner les cases de valeur 1"""
    for j, ligne in enumerate(niveau):

        for i, case in enumerate(ligne):
            if case == 1:
                surface.blit(mur, (i*25, j*25))

def from_coord_to_grid(pos):
# “””Retourne la position dans le niveau en indice (i, j) pos est un tuple contenant la position (x, y) du coin supérieur gauche. On limite i et j à être positif. “”” 
    x, y = pos 
    i = max(0, int(x // 25)) 
    j = max(0, int(y // 25)) 
    return i, j

def get_neighbour_blocks(niveau, i_start, j_start):
# “””Retourne la liste des rectangles autour de la position (i_start, j_start). Vu que le personnage est dans le carré (i_start, j_start), il ne peut entrer en collision qu’avec des blocks dans sa case, la case en-dessous, la case à droite ou celle en bas et à droite. On ne prend en compte que les cases du niveau avec une valeur de 1. “”” 
    blocks = list() 
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if niveau[j][i] == 1:
                topleft = i*25, j*25 
                blocks.append(pygame.Rect((topleft), (25, 25)))
            return blocks

def bloque_sur_collision(niveau, old_pos, new_pos, vx, vy):
# “””Tente de déplacer old_pos vers new_pos dans le niveau. S’il y a collision avec les éléments du niveau, new_pos sera ajusté pour être adjacents aux éléments avec lesquels il entre en collision. On passe également en argument les vitesses vx et vy. La fonction retourne la position modifiée pour new_pos ainsi que les vitesses modifiées selon les éventuelles collisions. “”” 
    old_rect = pygame.Rect(old_pos, (25, 25)) 
    new_rect = pygame.Rect(new_pos, (25, 25)) 
    i, j = from_coord_to_grid(new_pos) 
    collide_later = list() 
    blocks = get_neighbour_blocks(niveau, i, j) 
    for block in blocks:
        if not new_rect.colliderect(block):
            continue
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect) # Dans cette première phase, on n’ajuste que les pénétrations sur un # seul axe. if dx_correction == 0.0:
        new_rect.top += dy_correction 
        vy = 0.0

        if dy_correction == 0.0:
            new_rect.left += dx_correction 
            vx = 0.0
        else:
                collide_later.append(block)

        # Deuxième phase. On teste à présent les distances de pénétrations pour # les blocks qui en possédaient sur les 2 axes. for block in collide_later:
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect) 
        if dx_correction == dy_correction == 0.0:
            # Finalement plus de pénétration. Le new_rect a bougé précédemment lors d’une résolution de collision continu
            if abs(dx_correction) < abs(dy_correction):
                # Faire la correction que sur l’axe X (plus bas) 
                dy_correction = 0.0

            elif abs(dy_correction) < abs(dx_correction):
                # Faire la correction que sur l’axe Y (plus bas) 
                dx_correction = 0.0

        if dy_correction != 0.0:
            new_rect.top += dy_correction 
            vy = 0.0

        elif dx_correction != 0.0:
            new_rect.left += dx_correction 
            vx = 0.0    
            x, y = new_rect.topleft 
        return x, y, vx, vy

def compute_penetration(block, old_rect, new_rect):
# “””Calcul la distance de pénétration du new_rect dans le block donné. block, old_rect et new_rect sont des pygame.Rect. Retourne les distances dx_correction et dy_correction. “”” 
    dx_correction = dy_correction = 0.0 
    if old_rect.bottom <= block.top < new_rect.bottom:
        dy_correction = block.top - new_rect.bottom

    elif old_rect.top >= block.bottom > new_rect.top:
        dy_correction = block.bottom - new_rect.top

    if old_rect.right <= block.left < new_rect.right:
        dx_correction = block.left - new_rect.right

    elif old_rect.left >= block.right > new_rect.left:
        dx_correction = block.right - new_rect.left

    return dx_correction, dy_correction
    # Boucle événementielle continuer = True while continuer:
done = False                                                # Définition de la variable 'done' à False
while not done:                                             # Boucle tant que 'done' est différent de True        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vy = -20
    
        timer.tick(30) 
        keys_pressed = pygame.key.get_pressed() 
        # Sauvegarde de l’ancienne position 
        old_x, old_y = x, y 
        vx = (keys_pressed[pygame.K_d] - keys_pressed[pygame.K_q]) * 5 
        vy += pygame.GRAVITE 
        vy = min(20, vy) 
        # vy ne peut pas dépasser 25 sinon effet tunnel… 
        x += vx 
        y += vy 
        x, y, vx, vy = bloque_sur_collision(niveau, (old_x, old_y), (x, y), vx, vy)

    screen.fill(BLEU_NUIT) 
    dessiner_niveau(screen, niveau) 
    screen.blit(joueur, (x, y)) 
    pygame.display.flip()

pygame.quit()

# # “Théorème de la séparation des axes” 
# [SAT]= 'img/382e3984326883c92cb8c3c93bc85ced.jpg'
# # “Collision du joueur avec un mur” 
# [pos in grid]: img/Keysb.jpg
# # “Pénétration des rectangles.” 
# [penetration]: pygame_collisions_img/penetration.png
# # “Correction minimum”
# [min correction]: pygame_collisions_img/minimum_correction.png 