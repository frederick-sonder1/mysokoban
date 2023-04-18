import pygame

# Constantes pour les couleurs et la taille des tuiles
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 32
HEIGHT = 32
YELLOW_TILE_X = 4
YELLOW_TILE_Y = 4

# Carte du jeu
game_map = [
    [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,2,1,0,0,0,0,0,1],
    [1,0,0,4,0,0,1,7,1,0,0,4,0,0,1],
    [1,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
    [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [3,3,9,1,0,0,0,12,0,0,0,1,8,3,3],
    [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,5,0,0,0,1,1,1,0,0,0,0,0,1],
    [1,0,0,4,0,0,1,6,1,0,0,4,0,0,1],
    [1,0,0,0,0,0,1,2,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
]

class Tile(pygame.sprite.Sprite):                       # Définition de la classe 'Tile' qui hérite de la classe 'pygame.sprite.Sprite'
    def __init__(self, x, y, tile_type):                # constructeur de la classe 'Tile' avec les paramètres 'x', 'y' et 'tile_type'

        super().__init__()                              # Appel du constructeur parent => pygame.sprite.Sprite
        self.tile_type = tile_type                      # instanciation de la propriété 'tile_type' de la classe 'Tile' avec le param 'tile_type'
        self.image = pygame.Surface([WIDTH, HEIGHT])    # couleur de tuile ayant en param la surface d'une tuile
        self.rect = self.image.get_rect()               # instanciation de la propriété 'rect' de la classe 'Tile' avec le param 'rect'
        self.rect.x = x * WIDTH                         # instanciation de la propriété 'rect.x' de la classe 'Tile' avec le param 'x'
        self.rect.y = y * HEIGHT                        # instanciation de la propriété 'rect.y' de la classe 'Tile' avec le param 'y'

        if tile_type == 0:                              # Définition des couleurs du plateau
            self.image.fill('green')
        elif tile_type == 2:                            # Définition des couleurs du plateau
            self.image.fill('blue')
        elif tile_type == 3:                            # Définition des couleurs du plateau
            self.image.fill('blue')
        elif tile_type == 6:                            # Définition des couleurs du plateau
            self.image.fill('blue')
        elif tile_type == 7:                            # Définition des couleurs du plateau
            self.image.fill('blue')
        elif tile_type == 8:                            # Définition des couleurs du plateau
            self.image.fill('blue')
        elif tile_type == 9:                            # Définition des couleurs du plateau
            self.image.fill('blue')
        elif tile_type == 1:                            # Définition des couleurs du plateau
            self.image.fill('brown')
        elif tile_type == 4:                            # Définition des couleurs du plateau
            self.image.fill('yellow')
        elif tile_type == 5:                            # Définition des couleurs du plateau
            self.image.fill('black')
        elif tile_type == 10:                           # Définition des couleurs du plateau
            self.image.fill('blue')
        elif tile_type == 11:                           # Définition des couleurs du plateau
            self.image.fill('blue')
        self.tile_type = tile_type

    def is_movable(self):                               # Définition de la méthode 'is_movable' de la classe 'Tile'                           
        return self.tile_type == 4                      # pour savoir si la tuile est déplaçable

class Player(Tile, pygame.sprite.Sprite):               # Définition de la classe 'Player' qui hérite de la classe 'Tile' et de la classe 'pygame.sprite.Sprite'
    def __init__(self, x, y):                           # constructeur
        super().__init__(x, y, tile_type)               # Appel du constructeur parent => pygame.sprite.Sprite
        Tile.__init__(self, x, y, tile_type)            # Appel du constructeur parent => pygame.sprite.Sprite
        self.image = pygame.Surface([WIDTH, HEIGHT])    # couleur de tuile ayant en param la surface d'une tuile
        self.image.fill('red')                          # couleur de tuile ayant en param la surface d'une tuile
        self.rect = self.image.get_rect()               # instanciation de la propriété 'rect' de la classe 'Tile' avec le param 'rect'
        self.rect.x = x * WIDTH                         # instanciation de la propriété 'rect.x' de la classe 'Tile' avec le param 'x'
        self.rect.y = y * HEIGHT                        # instanciation de la propriété 'rect.y' de la classe 'Tile' avec le param 'y'

    def move(self, dx, dy):                             # Définition de la méthode 'move' de la classe 'Player'
        new_x = self.rect.x + dx * WIDTH                # Définition de la nouvelle position du joueur en x  
        new_y = self.rect.y + dy * HEIGHT               # Définition de la nouvelle position du joueur en y

        if new_x >= 0 and new_x < len(game_map[0]) * WIDTH and new_y >= 0 and new_y < len(game_map) * HEIGHT:   # Vérifier que la nouvelle position est dans la carte   
            if game_map[new_y // HEIGHT][new_x // WIDTH] == 0:      # Vérifier que la nouvelle position est sur une case vide, donc bouger le joueur                             
                self.rect.x = new_x                                 # Définition de la nouvelle position du joueur en x
                self.rect.y = new_y                                 # Définition de la nouvelle position du joueur en y
                return True                                         # Retourne True si le joueur a bougé
        return False
    
    def move_yellow_tile(self, djx, djy):                   # Définition de la méthode 'move_yellow_tile' de la classe 'Player'  
        new_x = self.rect.x + djx * WIDTH                   # Définition de la nouvelle position de la tuile en x  
        new_y = self.rect.y + djy * HEIGHT                  # Définition de la nouvelle position de la tuile en y               
    #     print('salut',self.tile_type)
    #     for tile in self.tile_type:                                     # Pour chaque tuile dans le groupe de sprites 'tiles'
    #         if tile == 4 and tile.rect.x // WIDTH == YELLOW_TILE_X and tile.rect.y // HEIGHT == YELLOW_TILE_Y:    # Vérifier que la tuile est jaune et qu'elle est à la position de la tuile jaune
    #             if direction == "LEFT":                             # si la direction est à gauche
    #                 tile.rect.x -= WIDTH                            # la tuile bouge à gauche
    #                 YELLOW_TILE_X -= 1                              # la tuile jaune bouge à gauche
    #             elif direction == "RIGHT":                          # Vérifier la direction
    #                 tile.rect.x += WIDTH                            # Déplacer la tuile
    #                 YELLOW_TILE_X += 1
    #             elif direction == "UP":
    #                 tile.rect.y -= HEIGHT
    #                 YELLOW_TILE_Y -= 1
    #             elif direction == "DOWN":
    #                 tile.rect.y += HEIGHT
    #                 YELLOW_TILE_Y += 1
    #             break
    
pygame.init()                                               # Initialisation de Pygame  

size = [WIDTH * len(game_map[0]), HEIGHT * len(game_map)]   # Définition de la taille de la fenêtre
screen = pygame.display.set_mode(size)                      # Définition de la taille de la fenêtre
tiles = pygame.sprite.Group()                               # Création d'un groupe de sprites
player = 5                                                  # Création d'un joueur 

for y, row in enumerate(game_map):                          # Création d'une boucle pour la création des tuiles
    for x, tile_type in enumerate(row):                     # Création d'une boucle pour la création des tuiles
        tile = Tile(x, y, tile_type)                        # Création d'une tuile
        tiles.add(tile)                                     # Ajout de la tuile au groupe de sprites
        if tile_type == 5:                                  # Si la tuile est de type 5, alors c'est le joueur
            player = Player(x, y)                           # Définition de la position du joueur

done = False                                                # Définition de la variable 'done' à False

while not done:                                             # Boucle tant que 'done' est différent de True        
    for event in pygame.event.get():                        # Boucle pour la gestion des événements
        if event.type == pygame.QUIT:                       # Si l'événement est de type 'pygame.QUIT', alors 'done' est True
            done = True             
        elif event.type == pygame.KEYDOWN:                  # Sinon si l'événement est de type 'pygame.KEYDOWN', alors le joueur bouge
            if event.key == pygame.K_q:                     # Si la touche est 'q', alors le joueur bouge vers la gauche
                player.move(-1, 0)                          # Déplacement du joueur vers la gauche
                # player.move_yellow_tile("LEFT")              # Déplacement de la tuile jaune vers la gauche
            elif event.key == pygame.K_d:                   # Si la touche est 'd', alors le joueur bouge vers la droite
                player.move(1, 0)                           # Déplacement du joueur vers la droite
                # player.move_yellow_tile("RIGHT")               # Déplacement de la tuile jaune vers la droite
            elif event.key == pygame.K_z:                   # Si la touche est 'z', alors le joueur bouge vers le haut
                player.move(0, -1)                          # Déplacement du joueur vers le haut
                # player.move_yellow_tile("UP")              # Déplacement de la tuile jaune vers le haut    
            elif event.key == pygame.K_s:                   # Si la touche est 's', alors le joueur bouge vers le bas
                player.move(0, 1)                           # Déplacement du joueur vers le bas
                # player.move_yellow_tile("DOWN")               # Déplacement de la tuile jaune vers le bas
    
    screen.fill(BLACK)                                      # Effacer l'écran
    tiles.draw(screen)                                      # Dessiner la carte       
    screen.blit(player.image, player.rect)                  # Dessiner le joueur
    pygame.display.flip()                                   # Mettre à jour l'affichage

pygame.quit()                                               # Fermer Pygame