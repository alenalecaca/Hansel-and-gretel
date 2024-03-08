#==========================================================
# EVOLUTIONS
# V1 (AR) creation des menus
#==========================================================

# Pyxel Studio

import pyxel, random


# le initialisations suivantes sont à faire
# ici si ce code principale est execute meme si c'est un module seconsaire
# par l'appel de la fonction menu_init depuis le module principal sinon
# dans tous les cas, laisser aussi ce code ici pour creation des variables globales

# parametrages des zones et initialisations des variables globales
# variable globale tableau des fonctions associees aux touche (on peut rallonger le tableau)
# chaque element correspont à une touche à afficher (tout marche pour tout nb d'element si rentre à l'ecran)
# chaque valeur correspond à un code de fonction à appeler, et à un code de graphique à afficher
menu_touches=[0,1,2,3]              #menu des fonction des touches courantes
# les fonctions correspondent aussi à un dessin
# le menu peut varier suivant le contexte

# parametrages des tailles de touches: constantes lisibles mais non modifiables par les fonctions
# tout marche si on change la taille des touches ou d'autre paramétres
# mais si on change la taille des touches, il faut les redessiner dans le fichier pyxres
lg_touche = 28                      # longueur d une touche 
ht_touche = 11                      # hauteur d'une touche
separ = 2                           # taille separateur entre touches
x_menu = 5                          # place en X du menu
y_menu = 90                         # place en Y du menu


########################################################################
############### FONCTIONS LOCALES ######################################
########################################################################
# zone_touche: calcule les intervalles de zone sensible d'une touche
# dit sur le point x,y est dans la zone de la touche num_touche
def zone_touche(num_touche,x,y):     #
    x_min = x_menu + num_touche*(lg_touche+separ)
    x_max = x_min + lg_touche
    y_min = y_menu
    y_max = y_menu + ht_touche
    if (x_min <= x <= x_max) and (y_min <= y <= y_max):
        return(True)
    else:
        return(False)
        
# fct_touche: dit si des coordonnées x_clic, y_click sont dans une zone sensible d'une touche,
# renvoie le code de la fonction de la touche si vrai, 255 si faux
# sera appelé à chaque click gauche de souris (dans "update")
def fct_touche(x_click,y_click):    
    for num_t in range(0,len(menu_touches)):    # tete la variable globale menu_touches
        if zone_touche(num_t,x_click,y_click):
            return(menu_touches[num_t])          # on prend la fonction contenue dans la touche i
    return(255)

# affiche_menu: affiche le menu complet de touches passé en parametres (longueur variable)
# va chercher dans le fichier pyxres le dessin associé au code fonction de chaque touche
# nb de touches (taille du tuple "menu"), taille des touches et séparateurs,
# peuvent êtres changés dans les variables globales, à condition de rentrer dans l'écran (pas de test)
def affiche_menu(menu):             # affiche les touches de "menu" (tableau)
    for ind in range(0,len(menu)):
        # afficher en x_menu+(numero touche * lg-touche), y_menu
        # le dessin situé en 0, ht_touche*code fonction
        # de taille lg_touche sur ht_touche
        pyxel.blt(x_menu+ind*(lg_touche+separ),y_menu,1,0,ht_touche*menu[ind],lg_touche,ht_touche)

                                
#==================================================================
# fonction à appeler dans la fonction "update" du module principal
#==================================================================
def menus_update():
    # GESTION DES MENUS
    # si click gauche souris, tester si sur une touche fonction
    global menu_touches

    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        fonction = fct_touche(pyxel.mouse_x,pyxel.mouse_y)
        print("valeur foncton =",fonction)    #### pour DEBUG: à enlever
      
        # et lancer la fonction si code connu
        if fonction == 0:
            # QUIT
            pyxel.quit()
        elif fonction == 1:
            # PLAY
            return(True)            # lancer le jeu, à affecer à "ingame"
        elif fonction == 2:
            # OPTIONS
            menu_touches=[4,5,6,7]  # menu options
        elif fonction == 3:
            # SHOP
            menu_touches=[0,1,2,3] # a remplacer menu SHOP ou action SHOP
        elif fonction == 4:
            # SOUND
            menu_touches=[0,1,2,3] # a remplacer menu SOUND ou fonction SOUND
        elif fonction == 5:
            # OPTION 2
            menu_touches=[0,1,2,3] # a remplacer menu Option2 ou fonction Option2       
        elif fonction == 6:
            # OPTION 3
            menu_touches=[0,1,2,3] # a remplacer menu Option3 ou fonction Option3       
        elif fonction == 7:
            # RETOUR DE OPTIONS
            menu_touches=[0,1,2,3] # on remet le menu principal (ne pas modifier)
        # completer avec des "elif" pour chaque fonction qui sera definie
        else:
            #
            print("fonction inconnue (255)",fonction)   #pour DEBUG, à enlever
        print(menu_touches)                             #pour DEBUG, à enlever

#=================================?????=====================================
# fonction à appeler à l'initialisation dans le module principal
# au cas ou le code principal de ce module seconadair n'est pas exécuté (?)
#===========================================================================
def menus_init():
    global menu_touches                 # tableau des codes fonctions des touches
    global lg_touche                    # longueur d une touche 
    global ht_touche                    # hauteur d'une touche
    global separ                        # taille separateur entre touches
    global x_menu                       # place en X du menu
    global y_menu                       # place en Y du menu

    pyxel.mouse(True)                   # rendre le curseur visible
    # pyxel.load("menus.pyxres")          # fichier ressources à renommer si besoin
    # parametrages des zones et initialisations des variables globales
    # variable globale tableau des fonctions associees aux touche (on peut rallonger le tableau)
    # chaque element correspont à une touche à afficher (tout marche pour tout nb d'element si rentre à l'ecran)
    # chaque valeur correspond à un code de fonction à appeler, et à un code de graphique à afficher
    menu_touches=[0,1,2,3]              #menu des fonction des touches courantes
    # les fonctions correspondent aussi à un dessin
    # le menu peut varier suivant le contexte

    # parametrages des tailles de touches: constantes lisibles mais non modifiables par les fonctions
    # tout marche si on change la taille des touches ou d'autre paramétres
    # mais si on change la taille des touches, il faut les redessiner dans le fichier pyxres
    lg_touche = 28                      # longueur d une touche 
    ht_touche = 11                      # hauteur d'une touche
    separ = 2                           # taille separateur entre touches
    x_menu = 5                          # place en X du menu
    y_menu = 90                         # place en Y du menu

#================================================================
# fonction à appeler dans la fonction "draw" du module principal
#================================================================
def menus_draw():
    global menu_touches

    pyxel.cls(0)                    # effacement ecran
    pyxel.rect(10, 10, 20, 20, 11)
    pyxel.rect(20,20,80,20,12)
    pyxel.text(30, 27, "Hansel & Gretel", 8 )
    pyxel.mouse(True)                   # rendre le curseur visible
    affiche_menu(menu_touches) 
        


        

            


