# Pyxel Studio

import pyxel, random

# initialisation à remplacer par celles du projet final
pyxel.init(128, 128)                #initialidstaion ecran 
pyxel.load("menus.pyxres")            # fichier ressources à renommer si besoin

pyxel.mouse(True)                   # rendre le curseur visible

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
ingame = False

lg_touche = 28                      # longueur d une touche 
ht_touche = 11                      # hauteur d'une touche
separ = 2                           # taille separateur entre touches
x_menu = 5                          # place en X du menu
y_menu = 90                         # place en Y du menu

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
        pyxel.blt(x_menu+ind*(lg_touche+separ),y_menu,0,0,ht_touche*menu[ind],lg_touche,ht_touche)


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
    if mort == True and btnp(pyxel.KEY_RETURN):
        mort = False

def fct_pause():
    if pause == False and btnp(pyxel.KEY_TAB) and not mort:
        pause = True
        saut = False
    elif pause == True and btnp(pyxel.KEY_TAB) and not mort:
        pause = False
                                
#==================================================================
# fonction à appeler dans la fonction "update" du module principal
#==================================================================
def menus_update():
    # GESTION DES MENUS
    # si click gauche souris, tester si sur une touche fonction
    global menu_touches
    global ingame
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        fonction = fct_touche(pyxel.mouse_x,pyxel.mouse_y)
        print("valeur foncton =",fonction)    #### pour DEBUG: à enlever
      
        # et lancer la fonction si code connu
        if fonction == 0:
            # QUIT
            pyxel.quit()
        elif fonction == 1:
            # PLAY
            ingame = True                   # a remplacer lancer le jeu
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
def menu_init():
    global menu_touches                 # tableau des codes fonctions des touches
    global lg_touche                    # longueur d une touche 
    global ht_touche                    # hauteur d'une touche
    global separ                        # taille separateur entre touches
    global x_menu                       # place en X du menu
    global y_menu                       # place en Y du menu
    global ingame
    pyxel.mouse(True)                   # rendre le curseur visible

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
    ingame = False
#================================================================
# fonction à appeler dans la fonction "draw" du module principal
#================================================================
def menu_draw():
   affiche_menu(menu_touches) 
        


####################################################################
################ simulation du module principal ####################
####################################################################
        
def update():                       #fonction de calcul periodique
    global blocs_liste

    # GESTION DES MENUS
    # appel de la fonction "update" du menu: à reporter dans module main
    if not ingame:
        menus_update()
    elif not mort and pause == True:
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
            
def draw(): 
    if not ingame:                      # fonction d'affichage periodique
        pyxel.cls(0)                    # effacement ecran
        pyxel.rect(10, 10, 20, 20, 11)
        pyxel.rect(20,20,80,20,12)
        pyxel.text(30, 27, "Hansel & Gretel", 8 )
     
    # appel de la fonction "draw" du menu: à reporter dans module main
        menu_draw()
    elif mort == True:
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


# appel de la fonction d'initialisation des parametres de menu
# a faire depuis module main si le code du corps du module "menu" n'est pas execute
# parceque c'est un module secondaire
menu_init()
pyxel.run(update, draw)
