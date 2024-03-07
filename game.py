# Pyxel Studio

import pyxel, random

# initialisation à remplacer par celles du projet final
# pyxel.init(128, 128)                #initialidstaion ecran 





# intialisations jeu

perso_x = 60
perso_y = 60
sol = 60
hauteur_perso = 8
saut = False
mort = False
pause = False

blocs_liste = []


########################################################################
############### FONCTIONS LOCALES ######################################
########################################################################

  
###### de app.py ###########
def blocs_creation(blocs_liste):
    """création aléatoire de blocs"""

    # un bloc par seconde
    if (pyxel.frame_count % 30 == 0):
        blocs_liste.append([120, random.randint(0, 120)])
    return blocs_liste

def blocs_deplacement(blocs_liste):
    """déplacement des blocs vers la gauche et suppression s'ils sortent du cadre"""
    """mouvement avec les touches de directions"""
#variables blocs provisoires, juste pour montrer l'effet de scrolling    
    for bloc in blocs_liste:
        bloc[0] -= 1
        if  bloc[0]<0:
            blocs_liste.remove(bloc)
    return blocs_liste

def perso_deplacement():
    global perso_y, sol, saut

    if pyxel.btnp(pyxel.KEY_UP) and perso_y == sol:
        saut = True
    if saut:
        perso_y -=3
        if perso_y <= 40:
            saut = False
    else:
        perso_y +=3
        if perso_y >= sol:
            perso_y = sol

def perso_mort():
    if perso_y >= sol:
        mort = False
    else:
        mort = True
        score = 0    #les point+compteur du score seront ajoutés après
        saut = False #nécessaire?

def menu_mort():
    global mort

    if mort == True and pyxel.btnp(pyxel.KEY_RETURN):
        mort = False

def fct_pause():
    pyxel.mouse(True)
    global pause
    global saut
    global mort

    if pause == False and pyxel.btnp(pyxel.KEY_TAB) and not mort:
        pause = True
        saut = False
    elif pause == True and pyxel.btnp(pyxel.KEY_TAB) and not mort:
        pause = False
                               
# def platforme(sol,perso x, perso y)
#if perso à tel endroit de la map:
#perso descend de tel carré selon la texture?
        
#=================================?????=====================================
# fonction à appeler à l'initialisation dans le module principal
# initialisations des fonctions de jeu
#===========================================================================
def game_init():
# intialisations jeu

    global perso_x
    global perso_y
    global sol
    global hauteur_perso
    global saut
    global mort
    global pause
    global blocs_liste

    # intialisations jeu
   
    perso_x = 60
    perso_y = 60
    sol = 60
    hauteur_perso = 8
    saut = False
    mort = False
    pause = False

    blocs_liste = []

  
    


#===================================================================================
# fonction à appeler dans la fonction "update" du module principal si ingame==True
#===================================================================================       
def game_update():                  #fonction de calcul periodique
    global blocs_liste
    global mort
    global pause

    if not mort and pause == True:
        for bloc in blocs_liste:
            bloc[0] -= 0    
    
    else:
        
        # creation des blocs
        blocs_liste = blocs_creation(blocs_liste)

        # mise a jour des positions des blocs
        blocs_liste = blocs_deplacement(blocs_liste)

        perso_deplacement()
        perso_mort()
        menu_mort()


#==================================================================================
# fonction periodique DRAW du jeu à appeler depuis le DRAW global si ingame==True =
#==================================================================================           
def game_draw(): 
    global mort
    global pause
    global perso_x
    global perso_y
    global blocs_liste
     
    pyxel.mouse(False)                   # rendre le curseur in visible

    #if perso à tel endroit de la map:
    #afficher la texture à rajouter au moment ou il y a une marche
    
    if mort == True:
        pyxel.cls(0)
        pyxel.text(20, 50, "Mort, appuie sur return pour recommencer", 7)

    elif mort == False and pause == True:
        pyxel.blt(perso_x, perso_y, 0, 0, 48, 13, 16, 2)
        
    else:
        
        # vide la fenetre
        pyxel.cls(0)

        # blocs
        for bloc in blocs_liste:
            pyxel.rect(bloc[0], bloc[1], 8, 8, 8)

        if pyxel.btn(pyxel.KEY_DOWN):
            if pyxel.frame_count % 15 < 5:
                pyxel.blt(perso_x, perso_y, 0, 14, 16, 16, 16, 2)
            elif pyxel.frame_count % 15 >= 5 and pyxel.frame_count % 15 < 10:
                pyxel.blt(perso_x, perso_y, 0, 14, 48, 16, 16, 2)
            else:
                pyxel.blt(perso_x, perso_y, 0, 14, 32, 16, 16, 2)
        else:  
            if pyxel.frame_count % 15 < 5:
                pyxel.blt(perso_x, perso_y, 0, 0, 48, 13, 16, 2)
            elif pyxel.frame_count % 15 >= 5 and pyxel.frame_count % 15 < 10:
                pyxel.blt(perso_x, perso_y, 0, 0, 32, 13, 16, 2)
            else:
                pyxel.blt(perso_x, perso_y, 0, 0, 64, 13, 16, 2)



