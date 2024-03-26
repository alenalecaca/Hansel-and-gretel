#==========================================================
# EVOLUTIONS
# V1 gestion perrso et blocs deco
# V2 (AR) demo jouable avec plateformes
# V3 (AR) correction de bugs, gestion sauts
#==========================================================

# Pyxel Studioplats_l

import pyxel, random

# Pyxel est initialisé dans le module principal
# par "pyxel.init(128, 128) ""               #initialidstaion ecran 


# intialisations jeu
difficulté = 1
perso_x = 60                # position X perso (à gauche)
perso_y = 60                # position Y perso (en haut)
sol = 76                    # position du sol à la position courante X du perso + sa hauteur
hauteur_perso = 16          # hauteur affichage personnage: toujours 16
taille_perso = 16           # taille su perso (pour future collisions front) 16 si debout, 11 si rampe
lg_perso = 13               # longueur en X du perso
h_debout = 16               # constante: hauteur perso debout
h_rampe = 11                # constante: hauteur perso rampant
saut = False
mort = False
pause = False
rampe = False
max_saut = 1                # hauteur max saut (haut gauche du perso)
sorciere_x=5                # position X de la sorcière (actuellement unité arbitraire)
sorciere_y=85               # position Y de la sorcière (actuellement unité arbitraire)

plats_liste = []      #liste des plateformes
                      # tableau de couples [X,Y] position haut gauche des plateformes
lg_plat = 40          # constante: longueur d'une plateforme = 5 carrés de 8
lg_trou = 24          # constante: longueur des trous entre plaeformes = 3 carrés de 8
ht_plat = 4           # constante: hauteur plateforme
restart = False         # redemarrer une session de jeu

plats_liste=[[10,perso_x+hauteur_perso],[65,perso_x+hauteur_perso]]  # premiers blocs pour ne pas tomber tout de suite

########################################################################
############### FONCTIONS LOCALES ######################################
########################################################################

#=======================================================================
# GESTION DES PLATEFORMES
#=======================================================================
def platforms_creation(plats_liste):
    """création aléatoire de plateformes"""
    global h_debout, ht_plat    # une plateforme toutes les X frame, a ajuster en fonction de la jouabilité
    if (pyxel.frame_count % 50 == 0):
        plats_liste.append([120, random.randint(0+h_debout+16, 128-ht_plat)])
    return plats_liste

def platforms_deplacement(plats_liste):
    """déplacement des plateformes vers la gauche et suppression s'ils sortent du cadre"""
    for plat in plats_liste:
        plat[0] -= 1                # on recule d'un pixel
        if  (plat[0]+lg_plat)<0:              # si la fin du bloc sort du cadre, on le supprime
            plats_liste.remove(plat)
    return plats_liste
  
def update_sol():
    global plats_liste
    global sol
    global lg_perso             # longueur en X du perso
    global perso_x              # position en X du debut du perso
    # on cherche si une plateforme est presente au niveau X du perso
    # si oui, on ajuste "sol" à la hauteur de cette plateforme
    exist_plat_en_x=False 
    plat_en_x = [0,0]           # pour debug
    plat=[0,0]                  # pour debug
    for plat in plats_liste:
        # pour chaque platefaorme, voir si elle est en position du perso
        # pour un meilleur rendu, on enleve quelques pixels de chque côté à la place occupée par le perso
    
        # pour etre sur la platforme ilfaut que le perso morde par sa droite de plus de 6 pixels sur la gauche de la plateforme
        #                                et que le perso soit encore sur sa gauche sur la plateforme de plus de 2 pixels
        if ((perso_x+lg_perso)>=plat[0]+2) and ((perso_x +2)<(plat[0]+lg_plat)):
            sol=plat[1]                          # alors le sol est defini par cette plateforme
            exist_plat_en_x = True
            plat_en_x = plat
    if not exist_plat_en_x:                           # sinon c'est un trou: on tombe
        sol = 128
    # DEBUG
    #print("exist plat = ", exist_plat_en_x)
    #print("plateforme en X = ", plat_en_x)
    #print("platforme ex x de ", plat_en_x[0]," a ", plat_en_x[0]+lg_plat)
    #print("sol= ",sol)
    #xxx=input("taper une touche pour continuer")
 
#========================================================================
# GESTION DU PERSONNAGE
#========================================================================
def perso_deplacement():
    global perso_x, perso_y, sol, saut, rampe, taille_perso, hauteur_perso, h_rampe, h_debout, max_saut, mort, score


    rampe = pyxel.btn(pyxel.KEY_DOWN) and (perso_y+hauteur_perso == sol)
    # mise à jour taille max personnage, pour  gestion collisions
    # pour l'affichage on affiche toujeur 16 pix de haut actuellement
    if rampe:
        taille_perso = h_rampe 
        perso_x += 1
    else:
        taille_perso = h_debout

    #gestion des sauts (monte en plusieurs fois jusqu'à la hauteur max_saut)
    
    if pyxel.btnp(pyxel.KEY_UP) and ((perso_y+hauteur_perso) == sol):
        saut = True
        score += 1                          # a confirmer =score = nombre de sauts
        print(" score = ", score)
    if saut:
        if pyxel.btnp(pyxel.KEY_UP,1,1):    # si la touche fleche est maintenue on continue à sauter
            perso_y -=3
            if perso_y <= max_saut:         # on a depassé la hauteur max (inversé): on retombe au sol
                saut = False
        else:
            saut = False
    else:
        if (perso_y+hauteur_perso)<=sol:
            perso_y = min(perso_y+3,sol-hauteur_perso)         # on est plus en saut, on retombe petit à petit au sol
        else:
            perso_y += 3
        if perso_y >= 128-hauteur_perso:         # si on est en bas: on est tombé, donc on est mort
            mort = True
         #   print("mort update")



def menu_mort():
    global mort, restart
    # si le personnage est mort, on attend un "return"
    if mort and pyxel.btnp(pyxel.KEY_RETURN):
        mort = False
        restart=True
    
    # il faut sans doute tout reinitialiser pour recommence, ou mettre ingame à False

def fct_pause():
    global pause, saut, mort

    if pause == False and pyxel.btnp(pyxel.KEY_TAB) and not mort:
        pause = True
        saut = False
    elif pause == True and pyxel.btnp(pyxel.KEY_TAB) and not mort:
        pause = False
                                

def sorciere():
    global mort, sorciere_x, sorciere_y, 
    if perso_x <= 40:                           #si le personnage passe 40px, la sorciere commence à descendre
        sorciere_y = sorciere_y - (40-perso_x)
    if perso_x >= 40 and perso_x < 60:
        sorciere_y =  sorciere_y - (40-perso_x)
    else:
        sorciere_y = 85

def perso_mort():
    if perso_x == sorciere_x and perso_y == sorciere_y:
        mort = True
        score = 0
        saut = False # necessaire?
    else:
        mort = False



#=================================?????=====================================
# fonction à appeler à l'initialisation dans le module principal
# initialisations des fonctions de jeu
#===========================================================================
def game_init():
# intialisations jeu

    global perso_x                # position personnage
    global perso_y                # position personnage
    global sol                    # hauteur (y) du sol courant (a la position x du personnage)
    global hauteur_perso          # hauteur du personnage pour affichage; toujours 16
    global lg_perso               # longueur en X du perso
    global taille_perso           # taille du personnage pour gere collisions front: 16 si debout, 11 si rampe
    global h_debout               # constante hauteur debout pour init
    global saut                   # "on est en train de sauter"
    global mort                   # "le personnage est mort"
    global pause                  # "le jeu est en pause"
    global rampe                  # "le personnage rampe"
    global plats_liste
    global max_saut               # hauteur max des suts (attention axe y inversé)
    global restart
    global score

    # intialisations jeu
   
    perso_x = 60                # position personnage
    perso_y = 60                # position personnage
    sol = 76                    # hauteur (y) du sol courant (a la position x du personnage+ sa hauteur)
    hauteur_perso = 16          # hauteur affichahge du personnage (toujours = 16)
    taille_perso = 16           # taille su perso (pour future collisions front) 16 si debout, 11 si rampe
    lg_perso = 13                # longueur en X du perso
    saut = False                # on est pas en saut
    mort = False                # on n'est pas mort
    pause = False               # on n'est pas en pause
    rampe = False               # on n'est pas en train de ramper
    max_saut = 1                # hauteur max des sauts (à parti du haut, inversé)
    score = 0
    sorciere_x=5
    sorciere_y=85

    blocs_liste = []            # liste des blocs (decor) à afficher, rien au depart

    plats_liste = []        #liste des plateformes
                            # tableau de couples [X,Y] position haut gauche des plateformes
    lg_plat = 40            # constante: longueur d'une plateforme = 5 carrés de 8
                            # plus tard on pourra faire les tailles variables
    lg_trou = 24            # constante: longueur des trous entre plaeformes = 3 carrés de 8
                            # pas utilisé pour l'instant (just un délai)
    ht_plat = 4             # constante: hauteur plateforme
                            # pas utilisé pour l'instant
    restart = False         # redemarrer une session de jeu
    
    plats_liste=[[10,perso_x+hauteur_perso],[65,perso_x+hauteur_perso]]  # premiers blocs pour ne pas tomber tout de suite


#===================================================================================
# fonction à appeler dan la fonction "update" du module principal si ingame==True
#===================================================================================       
def game_update():                  #fonction de calcul periodique
    global plats_liste
    global mort
    global pause
    global restart
    global mort
    global pause

   
    
    #else:                                       # on n'est pas en pause
        # creation des plateformes
    plats_liste = platforms_creation(plats_liste)
        # mise a jour des positions des blocs
    plats_liste = platforms_deplacement(plats_liste)

    update_sol()
    perso_deplacement()
    fct_pause()

     #   perso_mort()
    menu_mort()
    if restart:
        game_init() 
    return(True)            # affecté à ingame: on reste en jeu


#==================================================================================
# fonction periodique DRAW du jeu à appeler depuis le DRAW global si ingame==True =
#==================================================================================           
def game_draw(): 
    global mort
    global pause
    global perso_x
    global perso_y
    global plats_liste
    global rampe
     
    pyxel.mouse(False)                   # rendre le curseur in visible

    if mort:
        pyxel.cls(0)
        pyxel.text(15, 50, "MORT appuie sur return", 7)
        # print("mort main loop")

    elif pause:
        #vide pour le moment
        
    else:
        
        # vide la fenetre
        pyxel.cls(0)

        # plateformes
        for plat in plats_liste:
            pyxel.rect(plat[0], plat[1], lg_plat, ht_plat, 4)  # a remplacer par dessin pyxres
        # afficher personnage par effet progressif (3 trames)
        # en fonction de si il est debout/sautant ou rampant
        # on affiche sur hauteur 16 qqsoit le dessin
        if rampe:
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
