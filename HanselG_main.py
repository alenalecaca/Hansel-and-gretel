#==========================================================
# EVOLUTIONS
# V1 (AR) separation game et menus
#==========================================================


# Pyxel Studio

import pyxel, random
from menus import menus_init, menus_draw, menus_update
from game import game_init, game_draw, game_update

# initialisation globale
pyxel.init(128, 128)                   #initialidstaion ecran 
pyxel.load("res.pyxres")              # fichier ressources à renommer si besoin

ingame = False                          # = on est dans le jeu, donc pas dans le menu
                                        # si besoin on peut remplacer le booleen par une variable à plusieurs valeurs

####################################################################
################ module principal ####################
####################################################################
        
def update():                       #fonction de calcul periodique
    global ingame                   #etat "on est en jeu et pas en menu"

    # GESTION DES MENUS
    # appel de la fonction "update" du menu: à reporter dans module main
    if not ingame:
        ingame=menus_update()       # menus_update gere les menus et donne un resultat à affecter à "ingame" 
                                    # True si on a appuyé sur la touche PLAY
                                    # False sinon
    
    else:
        ingame=game_update()               # actuellement il n'y a rien de prevu pour rebasculer "ingame" à faux
                                    # si on le faisait on pourrait revenir à l'écran de menus
 
            
def draw(): 
    global ingame
    if not ingame:                      # fonction d'affichage periodique   
        # appel de la fonction "draw" du menu
        menus_draw()
       
    else:
        # appel de la fonction "draw" du jeu
        game_draw()



# appel des fonctions d'initialisation du menu et du jeu

menus_init()                # initialiser les menus
game_init()                 # initialiser le jeu
pyxel.run(update, draw)
