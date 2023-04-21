import pygame               # imprort de la librairie pygame
import random               # import de la librairie random

pygame.init()               # initialisation de pygame

# Définition des variables de taille
width = 650
height = 700
pixel = 64  

screen = pygame.display.set_mode((width, height))   # Définition de la taille de la fenêtre
pygame.display.set_caption("Pousse ta tuile")       # Définition du titre de la fenêtre
gameIcon = pygame.image.load('brick-wall.png')      # Définition de l'icône de la fenêtre (image)
pygame.display.set_icon(gameIcon)                   # Affichage de l'icône sur l'objet écran (fenêtre)

backgroundImg = pygame.image.load("brick-wall.png") # Définition de l'image de fond
blockImage = pygame.image.load("cube.png")          # Définition de l'image du bloc
playerImage = pygame.image.load("player.png")       # Définition de l'image du joueur

playerXPosition = (width/2) - (pixel/2)             # Définition de la position initiale du joueur en X (au milieu de l'écran)
playerYPosition = height - pixel - 10	            # Définition de la position initiale du joueur en Y (en bas de l'écran)
playerXPositionChange = 0                           # Définition de la variable de changement de position du joueur en X (initialisée à 0)

blockXPosition = random.randint(0,(width - pixel))  # Définition de la position initiale du bloc en X (aléatoire)
blockYPosition = random.randint(0,(width - pixel))  # Définition de la position initiale du bloc en Y (en haut de l'écran)
blockXPositionChange = 0                            # Définition de la variable de changement de position du bloc en X (initialisée à 0)
blockYPositionChange = 2                            # Définition de la variable de changement de position du bloc en Y (initialisée à 2)

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////// Fonctions //////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////

# ////////// Fonction pour afficher l'image du joueur //////////
def player(x, y):                                   # Définition de la fonction pour afficher l'image du joueur
    screen.blit(playerImage, (x, y))                # Affichage de l'image sur l'objet écran

# ////////// Fonction pour afficher l'image du bloc //////////
def block(x, y):                                    # Définition de la fonction pour afficher l'image du bloc
    screen.blit(blockImage,(x, y))                  # Affichage de l'image sur l'objet écran

# ////////// Fonction pour détecter la collision //////////
def crash():                                                            # Définition de la fonction pour détecter la collision
    global blockYPosition                                               # Définition de la variable blockYPosition comme globale
    if playerYPosition < (blockYPosition + pixel):                      # Si la position du joueur en Y est inférieure à la position du bloc en Y + la taille d'un pixel
        if ((playerXPosition > blockXPosition                           # Si la position du joueur en X est supérieure à la position du bloc en X
            and playerXPosition < (blockXPosition + pixel))             # Et la position du joueur en X est inférieure à la position du bloc en X + la taille d'un pixel
            or ((playerXPosition + pixel) > blockXPosition              # Ou la position du joueur en X + la taille d'un pixel est supérieure à la position du bloc en X
            and (playerXPosition + pixel) < (blockXPosition + pixel))): # Et la position du joueur en X + la taille d'un pixel est inférieure à la position du bloc en X + la taille d'un pixel

            blockYPosition = height + 1000                              # On déplace le bloc en dehors de l'écran


# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////// Boucle Principale ///////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
running = True                                                  # Définition de la variable running comme True
while running:                                                  # Tant que running est True
    screen.blit(backgroundImg, (0, 0))                          # Affichage de l'image de fond sur l'objet écran
    for event in pygame.event.get():                            # Pour chaque événement dans la liste des événements
        if event.type == pygame.QUIT:                           # Si l'événement est de type QUIT
            pygame.quit()                                       # On quitte pygame
        if event.type == pygame.KEYDOWN:                        # Si l'événement est de type KEYDOWN
            if event.key == pygame.K_RIGHT:                     # Si la touche pressée est la flèche de droite
                playerXPositionChange = 3                       # On augmente la variable de changement de position du joueur en X de 3
            if event.key == pygame.K_LEFT:                      # Si la touche pressée est la flèche de gauche
                playerXPositionChange = -3                      # On diminue la variable de changement de position du joueur en X de 3
        if event.type == pygame.KEYUP:                          # Si l'événement est de type KEYUP
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:    # Si la touche pressée est la flèche de droite ou la flèche de gauche
                playerXPositionChange = 0                       # On remet la variable de changement de position du joueur en X à 0

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////// Limite Joueur ///////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////

# ////////// Limite droite //////////
if playerXPosition >= (width - pixel):              # Si la position du joueur en X est supérieure à la largeur de l'écran - la taille d'un pixel
    playerXPosition = (width - pixel)               # On remet la position du joueur en X à la largeur de l'écran - la taille d'un pixel

# ////////// Limite gauche //////////
if playerXPosition <= 0:                            # Si la position du joueur en X est inférieure à 0
    playerXPosition = 0                             # On remet la position du joueur en X à 0

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////// Limite Bloc /////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////

if (blockYPosition >= height - 0 and blockYPosition <= (height + 200)):     # Si la position du bloc en Y est supérieure à la hauteur de l'écran - 0
    blockYPosition = 0 - pixel                                              # On remet la position du bloc en Y à 0 - la taille d'un pixel
    blockXPosition = random.randint(0, (width - pixel))                     # On assigne une valeur aléatoire à la position du bloc en X
    playerXPosition += playerXPositionChange                                # On ajoute la variable de changement de position du joueur en X à la position du joueur en X
    blockYPosition += blockYPositionChange                                  # On ajoute la variable de changement de position du bloc en Y à la position du bloc en Y
    player(playerXPosition, playerYPosition)                                # Appel de la fonction pour afficher l'image du joueur
    block(blockXPosition, blockYPosition)                                   # Appel de la fonction pour afficher l'image du bloc
    crash()                                                                 # Appel de la fonction pour détecter la collision

pygame.display.update()                 # Mise à jour de l'objet écran
