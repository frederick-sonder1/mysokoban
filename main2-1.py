import pygame

# Constantes pour les couleurs et la taille des tuiles
WIDTH = 32
HEIGHT = 32
crave = pygame.image.load('hasty-grave.png')                # Création d'une tuile avec une image
tomb = pygame.image.load('tombstone.png')                   # Création d'une tuile avec une image
wall = pygame.image.load('stone-wall.png')                  # Création du mur avec une image
cube = pygame.image.load('cube.png')                        # Création du cube avec une image
playerImg = pygame.image.load('player.png')                 # Création du joueur avec une image
finish = pygame.image.load('finish-line.png')               # Création de la fin avec une image
grass =pygame.image.load('grass.png')                       # Création de l'herbe avec une image transparente 

# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////// Map ////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# Carte du jeu
game_map = [
    [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,2,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,7,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
    [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [3,3,9,1,0,0,0,12,0,0,0,1,8,3,3],
    [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
    [5,0,0,0,0,0,1,6,1,0,0,4,0,0,1],
    [1,0,0,0,0,0,1,2,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
]

# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////// Tuiles /////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
class Tile(pygame.sprite.Sprite):                               # Définition de la classe 'Tile' qui hérite de la classe 'pygame.sprite.Sprite'
    def __init__(self, x, y, tile_type):                        # constructeur de la classe 'Tile' avec les paramètres 'x', 'y' et 'tile_type'

        super().__init__()                                      # Appel du constructeur parent => pygame.sprite.Sprite
        self.tile_type = tile_type                              # instanciation de la propriété 'tile_type' de la classe 'Tile' avec le param 'tile_type'
        self.image = pygame.Surface([WIDTH, HEIGHT])            # couleur de tuile ayant en param la surface d'une tuile
        self.rect = self.image.get_rect()                       # instanciation de la propriété 'rect' de la classe 'Tile' avec le param 'rect'
        self.rect.x = x * WIDTH                                 # instanciation de la propriété 'rect.x' de la classe 'Tile' avec le param 'x'
        self.rect.y = y * HEIGHT                                # instanciation de la propriété 'rect.y' de la classe 'Tile' avec le param 'y'

    def is_yellow(self):                                        # Définition de la méthode 'is_yellow' de la classe 'YellowTile'                           
        return False                                             # pour savoir si la tuile est jaune
    
    def image(self):                                            # Définition de la méthode 'image' de la classe 'YellowTile'
        new_x = self.rect.x + x * WIDTH                         # Définition de la nouvelle position de la tuile en x  
        new_y = self.rect.y + y * HEIGHT                        # Définition de la nouvelle position de la tuile en y  
        if game_map[new_y // HEIGHT][new_x // WIDTH] == 4:
            self.image = cube    


# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////// Caisse /////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
class YellowTile(Tile, pygame.sprite.Sprite):                           # Définition de la classe 'YellowTile' qui hérite de la classe 'Tile'
    def __init__(self, x, y):                                           # constructeur de la classe 'YellowTile' avec les paramètres 'x' et 'y'
        super().__init__(x, y, tile_type)                               # Appel du constructeur parent => Tile
        Tile.__init__(self, x, y, tile_type)                            # Appel du constructeur parent => pygame.sprite.Sprite
        self.image = pygame.Surface([WIDTH, HEIGHT])                    # couleur de tuile ayant en param la surface d'une tuile
        self.image = pygame.image.load('cube.png')    
        self.rect = self.image.get_rect()                               # instanciation de la propriété 'rect' de la classe 'YellowTile' avec le param 'rect'
        self.rect.x = x * WIDTH                                         # instanciation de la propriété 'rect.x' de la classe 'YellowTile' avec le param 'x'
        self.rect.y = y * HEIGHT                                        # instanciation de la propriété 'rect.y' de la classe 'YellowTile' avec le param 'y'
        self.is_yellow = True                                           # instanciation de la propriété 'is_yellow' de la classe 'YellowTile' avec le param 'is_yellow'
        self.tile_type = tile_type                                      # instanciation de la propriété 'tile_type' de la classe 'YellowTile' avec le param 'tile_type' 

    def is_movable(self):                                               # Définition de la méthode 'is movable' de la classe 'YellowTile' 
        new_x1 = self.rect.x + x * WIDTH                                # Définition de la nouvelle position de la tuile en x  
        new_y1 = self.rect.y + y * HEIGHT                               # Définition de la nouvelle position de la tuile en y               
        position = game_map[new_y1 // HEIGHT][new_x1 // WIDTH]          # Définition de la position de la tuile 
        if position == 4:                                               # Vérifier que la nouvelle position est sur une case jaune, donc bouger la tuile
            tile = Tile(new_x1, new_y1, 4)                              # Définition de la nouvelle position de la tuile
            tile.rect.x = new_x1+1                                      # Définition de la nouvelle position de la tuile en x
            tile.rect.y = new_y1+1                                      # Définition de la nouvelle position de la tuile en y
            position = 0                                                # Définition de la nouvelle position de la tuile sur la carte
            game_map[self.rect.y // HEIGHT][self.rect.x // WIDTH] = 4   # Définition de la nouvelle position de la tuile sur la carte
            game_map[new_y1 // HEIGHT][new_x1 // WIDTH] = 0             # Définition de la nouvelle position de la tuile sur la carte
            r = tile.is_yellow()
            print('isYellow3?', r)    
            return True                                                 # Retourne True si le joueur a bougé                      
        return False                                                    # pour savoir si la tuile est déplaçable

    
# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////// Joueur/se //////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
class Player(Tile, pygame.sprite.Sprite):                       # Définition de la classe 'Player' qui hérite de la classe 'Tile' et de la classe 'pygame.sprite.Sprite'
    def __init__(self, x, y):                                   # constructeur
        super().__init__(x, y, tile_type)                       # Appel du constructeur parent => pygame.sprite.Sprite
        Tile.__init__(self, x, y, tile_type)                    # Appel du constructeur parent => pygame.sprite.Sprite
        self.image = pygame.Surface([WIDTH, HEIGHT])            # couleur de tuile ayant en param la surface d'une tuile
        self.image = playerImg
        self.rect = self.image.get_rect()                       # instanciation de la propriété 'rect' de la classe 'Tile' avec le param 'rect'
        self.rect.x = x * WIDTH                                 # instanciation de la propriété 'rect.x' de la classe 'Tile' avec le param 'x'
        self.rect.y = y * HEIGHT                                # instanciation de la propriété 'rect.y' de la classe 'Tile' avec le param 'y'
        self.tile_type = tile_type                              # instanciation de la propriété 'tile_type' de la classe 'Tile' avec le param 'tile_type'


    def move(self, x, y):                                       # Définition de la méthode 'move_yellow_tile' de la classe 'Player'   
        new_x = self.rect.x + x * WIDTH                         # Définition de la nouvelle position de la tuile en x  
        new_y = self.rect.y + y * HEIGHT                        # Définition de la nouvelle position de la tuile en y               
        position = game_map[new_y // HEIGHT][new_x // WIDTH]    # Définition de la position de la tuile
        # for y, row in enumerate(game_map):                          # Création d'une boucle pour la création des tuiles
        #     for x, tile_type in enumerate(row):                     # Création d'une boucle pour la création des tuiles
        #         while tile_type == 12:                                 # Si la tuile n'est pas de type 12, alors c'est la caisse
        #             tile = Tile(x, y, tile_type)
        #             print('tileeeeeeeeeeeeeeeeee', tile.tile_type)
        #             # pygame.QUIT()   
        if new_x >= 0 and new_x < len(game_map[0]) * WIDTH and new_y >= 0 and new_y < len(game_map) * HEIGHT:   # Vérifier que la nouvelle position est dans la carte   
            
            if position == 4:                                                   # Vérifier que la nouvelle position est sur une case jaune, donc bouger la tuile  
                    tile = Tile(new_x, new_y, 4)                                # Définition de la nouvelle position de la tuile
                    tile.rect.x = new_x                                         # Définition de la nouvelle position de la tuile en x
                    tile.rect.y = new_y                                         # Définition de la nouvelle position de la tuile en y
                    self.image = cube
                    position = 0                                                # Définition de la nouvelle position de la tuile sur la carte
                    game_map[self.rect.y // HEIGHT][self.rect.x // WIDTH] = 4   # Définition de la nouvelle position de la tuile sur la carte                
                    game_map[new_y // HEIGHT][new_x // WIDTH] = 0               # Définition de la nouvelle position de la tuile sur la carte
                    r = tile.is_yellow()
                    print('isYellow?', r)
                    print('move déplacement-caisse')
                    return True                                                 # Retourne True si le joueur a bougé 
            if position == 0:                                                   # Vérifier que la nouvelle position est sur une case vide, donc bouger le joueur      
                    tile = Tile(new_x, new_y, 5)                                # Définition de la nouvelle position de la tuile    
                    self.image = playerImg
                    tile.rect.x = new_x                                         # Définition de la nouvelle position de la tuile en x
                    tile.rect.y = new_y                                         # Définition de la nouvelle position de la tuile en y                   
                    self.rect.x = new_x                                         # Définition de la nouvelle position du joueur en x
                    self.rect.y = new_y                                         # Définition de la nouvelle position du joueur en y
                    game_map[self.rect.y // HEIGHT][self.rect.x // WIDTH] = 5   # Définition de la nouvelle position de la tuile sur la carte
                    game_map[new_y // HEIGHT][new_x // WIDTH] = 0               # Définition de la nouvelle position de la tuile sur la carte
                    print('move déplacement')
                    r = tile.is_yellow()
                    print('isYellow2?', r)
                    return True                                                 # Retourne True si le joueur a bougé
            if position == 12:
                    tile = Tile(new_x, new_y, 4)                                # Définition de la nouvelle position de la tuile    
                    self.image = playerImg
                    tile.rect.x = new_x                                         # Définition de la nouvelle position de la tuile en x
                    tile.rect.y = new_y                                         # Définition de la nouvelle position de la tuile en y                   
                    self.rect.x = new_x                                         # Définition de la nouvelle position du joueur en x
                    self.rect.y = new_y                                         # Définition de la nouvelle position du joueur en y
                    game_map[self.rect.y // HEIGHT][self.rect.x // WIDTH] = 12  # Définition de la nouvelle position de la tuile sur la carte
                    game_map[new_y // HEIGHT][new_x // WIDTH] = 12              # Définition de la nouvelle position de la tuile sur la carte
                    print('move déplacement')
                    r = tile.is_yellow()
                    print('isYellow2?', r)
                    return True        
        print('move déplacement-bloqué')
        return False                                                            # Retourne False si le joueur n'a pas bougé
    
pygame.init()                                               # Initialisation de Pygame  

size = [WIDTH * len(game_map[0]), HEIGHT * len(game_map)]   # Définition de la taille de la fenêtre
screen = pygame.display.set_mode(size)                      # Définition de la taille de la fenêtre
tiles = pygame.sprite.Group()                               # Création d'un groupe de sprites


# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////// Création de la carte //////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////

# Création d'une boucle pour la création des tuiles
for y, row in enumerate(game_map):                          # Création d'une boucle pour la création des tuiles
    for x, tile_type in enumerate(row):                     # Création d'une boucle pour la création des tuiles
        tile = Tile(x, y, tile_type)                        # Création d'une tuile
        tiles.add(tile)                                     # Ajout de la tuile au groupe de sprites
        if tile_type == 0:                                  # Définition de la couleur de la tuile en fonction de la valeur de la carte
            tile.image = grass     
        elif tile_type == 2:                                    
            tile.image = crave     
        elif tile_type == 3:                                    
            tile.image = crave     
        elif tile_type == 6:                                    
            tile.image = tomb     
        elif tile_type == 7:                                    
            tile.image = tomb     
        elif tile_type == 8:                                    
            tile.image = crave     
        elif tile_type == 9:                                    
            tile.image = tomb     
        elif tile_type == 1:                                    
            tile.image = wall         
        elif tile_type == 5:                                    
            tile.image.fill('black')   
        elif tile_type == 10:                                   
            tile.image = crave     
        elif tile_type == 11:                                   
            tile.image = crave
        elif tile_type == 12:                                   
            tile.image = finish
        tile.tile_type = tile_type

        if tile_type == 5:                                  # Si la tuile est de type 5, alors c'est le joueur
            player = Player(x, y)                           # Définition de la position du joueur
        if tile_type == 4:                                  # Si la tuile est de type , alors c'est la caisse
            caisse = YellowTile(x, y)                       # Définition de la position de la caisse


                        

# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////// Déplacement ////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////
done = False                                        # Définition de la variable 'done' à False
while not done:                                     # Boucle tant que 'done' est différent de True        
    
    for event in pygame.event.get():                # Boucle pour la gestion des événements
       
        if event.type == pygame.QUIT:               # Si l'événement est de type 'pygame.QUIT', alors 'done' est True
            done = True             
        elif event.type == pygame.KEYDOWN:          # Sinon si l'événement est de type 'pygame.KEYDOWN', alors le joueur bouge
            
            if event.key == pygame.K_q:             # Si la touche est 'q', alors le joueur bouge vers la gauche
                player.move(-1, 0)                  # Déplacement du joueur vers la gauche
                print('mapG', game_map)
                pygame.display.flip()               # Mettre à jour l'affichage
            elif event.key == pygame.K_d:           # Si la touche est 'd', alors le joueur bouge vers la droite
                player.move(1, 0)                   # Déplacement du joueur vers la droite
                print('mapD', game_map)
                pygame.display.flip()               # Mettre à jour l'affichage
            elif event.key == pygame.K_z:           # Si la touche est 'z', alors le joueur bouge vers le haut
                player.move(0, -1)                  # Déplacement du joueur vers le haut
                print('mapH', game_map)
                pygame.display.flip()               # Mettre à jour l'affichage
            elif event.key == pygame.K_s:           # Si la touche est 's', alors le joueur bouge vers le bas
                player.move(0, 1)                   # Déplacement du joueur vers le bas
                print('mapB', game_map)
                pygame.display.flip()               # Mettre à jour l'affichage
    
    tiles.draw(screen)                              # Dessiner la carte       
    screen.blit(player.image, player.rect)          # Dessiner le joueur
    screen.blit(caisse.image, caisse.rect)          # Dessiner la caisse
    pygame.display.flip()                           # Mettre à jour l'affichage

pygame.quit()                                       # Fermer Pygame