# Pyxel Studio
import pyxel, random
 

# taille de la fenetre en pixels
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du personnage, seuil de base du sol et la hauteur du personnage
perso_x = 60
perso_y = 60
sol = 60
hauteur_perso = 8
saut = False

blocs_liste = []

#variable difficulté en fonction du temps (à venir)
# dif = ...

#variables blocs provisoires, juste pour montrer l'effet de scrolling
def blocs_creation(blocs_liste):
    """création aléatoire de blocs"""

    # un bloc par seconde
    if (pyxel.frame_count % 30 == 0):
        blocs_liste.append([120, random.randint(0, 120)])
    return blocs_liste

def blocs_deplacement(blocs_liste):
    """déplacement des blocs vers la gauche et suppression s'ils sortent du cadre"""
    """mouvement avec les touches de directions"""
    
    for bloc in blocs_liste:
        bloc[0] -= 1
        if  bloc[1]>128:
            blocs_liste.remove(bloc)
    return blocs_liste

def perso_deplacement():
    global perso_y, sol, saut

    if pyxel.btnp(pyxel.KEY_UP) and perso_y == sol:
        saut = True
    if saut:
        perso_y -=5
        if perso_y <= 40:
            saut = False
    if not saut:
        perso_y +=3
        if perso_y >= sol:
            perso_y = sol
    


def update():
    global blocs_liste, perso_y

    # creation des blocs
    blocs_liste = blocs_creation(blocs_liste)

    # mise a jour des positions des blocs
    blocs_liste = blocs_deplacement(blocs_liste)

    perso_deplacement()


def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # perso (carre 8x8)
    if pyxel.btn(pyxel.KEY_DOWN):
        pyxel.rect(perso_x, perso_y+4, 8, 4, 1)
    else: pyxel.rect(perso_x, perso_y, 8, 8, 1)

    # blocs
    for bloc in blocs_liste:
        pyxel.rect(bloc[0], bloc[1], 8, 8, 8)


help(pyxel.rect)

pyxel.run(update, draw)