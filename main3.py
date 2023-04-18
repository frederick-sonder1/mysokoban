import pygame

# Constantes pour les couleurs et la taille des tuiles
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 32
HEIGHT = 32

# Créer la carte du jeu
def _generer():

    mur = 1
    sol = 0
    exit = 2

    game_map = []

    niv = []
    for ligne in fichier:
        ligne_niv = []
        for i in ligne:
            if i != '\n':
                ligne_niv.append(i)
        niv.append(ligne_niv)
    fichier.close()

    num_ligne = 0
    for ligne in niv:
        num_case = 0
        for i in ligne:
            if i == 'W':
                game_map.append(py.Rect(54*num_case, 54*num_ligne, mur.get_width(), mur.get_height()))
                fenetre.blit(mur, (54*num_case,54*num_ligne))
            elif i == 'F':
                fenetre.blit(sol, (54*num_case,54*num_ligne))
            elif i == 'E':
                fenetre.blit(exit, (54*num_case,54*num_ligne))
                exitRect = exitRect.move(54*num_case,54*num_ligne)
            num_case += 1
        num_ligne += 1
        game_map

# game_map = [
#     [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,1,2,1,0,0,0,0,0,1],
#     [1,0,0,4,0,0,1,7,1,0,0,4,0,0,1],
#     [1,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
#     [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
#     [3,3,9,1,0,0,10,12,10,0,0,1,8,3,3],
#     [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
#     [1,0,5,0,0,0,1,1,1,0,0,0,0,0,1],
#     [1,0,0,4,0,0,1,6,1,0,0,4,0,0,1],
#     [1,0,0,0,0,0,1,2,1,0,0,0,0,0,1],
#     [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
# ]

# Définir la classe pour les éléments de la carte
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type):                # constructeur

        super().__init__()                              # Appel du constructeur parent => pygame.sprite.Sprite
        self.tile_type = tile_type                      # instanciation de la propriété 'tile_type' de la classe 'Tile' avec le paramètre 'tile_type'
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.x = x * WIDTH
        self.rect.y = y * HEIGHT
        if tile_type == 0:
            self.image.fill('green')
        elif tile_type == 2:
            self.image.fill('blue')
        elif tile_type == 3:
            self.image.fill('blue')
        elif tile_type == 6:
            self.image.fill('blue')
        elif tile_type == 7:
            self.image.fill('blue')
        elif tile_type == 8:
            self.image.fill('blue')
        elif tile_type == 9:
            self.image.fill('blue')
        elif tile_type == 1:
            self.image.fill('brown')

        self.tile_type = tile_type


# Définir la classe pour le joueur
class Player(Tile, pygame.sprite.Sprite):
#     Tile = Tile(pygame.sprite.Sprite)
    def __init__(self, x, y):
        super().__init__(x, y, tile_type)
        Tile.__init__(self, x, y, tile_type)

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.x = x * WIDTH
        self.rect.y = y * HEIGHT
    def move(self, dx, dy):
        new_x = self.rect.x + dx * WIDTH
        new_y = self.rect.y + dy * HEIGHT

        if new_x >= 0 and new_x < len(game_map[0]) * WIDTH and new_y >= 0 and new_y < len(game_map) * HEIGHT:
            # Vérifier que la nouvelle position est sur une case vide, donc bouger le joueur
            if game_map[new_y // HEIGHT][new_x // WIDTH] == 0:
                self.rect.x = new_x
                self.rect.y = new_y
                return True
        return False

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
# size = [WIDTH * len(game_map[0]), HEIGHT * len(game_map)]
# screen = pygame.display.set_mode(size)

# Créer les sprites pour la carte et le joueur
tiles = pygame.sprite.Group()
player = None
for y, row in enumerate(_generer()):
    for x, tile_type in enumerate(row):
        tile = Tile(x, y, tile_type)
        tiles.add(tile)
        if tile_type == 5:
            player = Player(x, y)


# Boucle principale du jeu
done = False
while not done:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                player.move(-1, 0)
            elif event.key == pygame.K_d:
                player.move(1, 0)
            elif event.key == pygame.K_z:
                player.move(0, -1)
            elif event.key == pygame.K_s:
                player.move(0, 1)

    # Effacer l'écran et redessiner la carte et le joueur
    screen.fill(BLACK)
    tiles.draw(screen)
    screen.blit(player.image, player.rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Fermer Pygame
pygame.quit()