import pyxel
import random
import numpy as np

#####################################################################################################
############### FONCTION D INITIALISATION ###########################################################
############### a appeler depuis module principal au demarrage ou redemarrage #######################
#####################################################################################################
def game_init():
# intialisations jeu

    global perso_x                # position personnage
    global perso_y                # position personnage
    global sol                    # hauteur (y) du sol courant (a la position x du personnage)
    global hauteur_perso          # hauteur du personnage pour affichage; toujours 16
    global lg_perso               # longueur en X du perso
    global lg_rampe               # longueur du personnage lorce qu'il rampe
    global taille_perso           # taille du personnage pour gere collisions front: 16 si debout, 11 si rampe
    global h_debout, h_rampe      # constante hauteur debout pour init
    global saut                   # "on est en train de sauter"
    global mort                   # "le personnage est mort"
    global rampe                  # "le personnage rampe"
    global plats_liste            # liste des plateformes
    global ht_plat,lg_plat        # hauteur et longueur des plateformes
    global max_saut               # hauteur max des sauts (attention axe y inversé)
    global restart                # redemarrer une session de jeu
    global score                  # score du la partie
    global difficulté             # utilisé pour calculer le score et la difficulté au file de la partie
    global count                  # compteur basique
    global plancher, sol_bas      # hauteur plancher (terre) et hauteur du sol du bas (plancher ou obstacle)
    global obst_liste             # liste des obstacles [[x,type],...]
    global obst_types             # description reference des types d'obstacles [[long,haut,traversable],...]
    
    perso_x = 60          
    perso_y = 60           
    sol = 76                   
    hauteur_perso = 16        
    taille_perso = 16          
    lg_perso = 13             
    lg_rampe = 16
    h_debout = 16              
    h_rampe = 11                
    saut = False 
    rampe = False 

    mort = False                
    restart = False               
                 
    max_saut = 1                
    difficulté = np.e
    score = 0
    count = 0

    # gestion des plateformes
    plats_liste=[[10,perso_y+hauteur_perso,0],[65,perso_y+hauteur_perso,1]]  # premiers plateformes pour ne pas tomber tout de suite  
    lg_plat = 40       
    ht_plat = 8         
    
    # gestion du sol bas et des obstacles
    plancher = 124             
    sol_bas = 124            
    obst_liste = []
    # [largeur, hauteur, mortel, posx, posy] à mettre à jour après design des obstacles
    obst_types = [[16,16,False,0,0],    # chat
                  [13,16,True,17,0],    # fiole
                  [13,16,True,33,0],    # marmite
                  [16,13,False,48,2],   # araignee
                  [13,16,False,67,0],   # sucre d'orge
                  [14,12,False,82,4],   # bonbon
                  [16,15,True,96,1]]    # champignon

#####################################################################################################
############### FONCTIONS LOCALES ###################################################################
#####################################################################################################

#=======================================================================
# GESTION DES OBSTACLES
#=======================================================================
def obstacles_creation(obst_liste):
    """création aléatoire d'obstacles au sol"""
    global obst_types
    if pyxel.frame_count % (70/int(np.log(difficulté))) == 0 and random.randint(1,100) <= 75:  # génération aléatoire des obstacles toutes les 60 frames (en dépendant de la difficulté pour que les intervalles restent les mêmes)
        obst_liste.append([120, random.randint(0,len(obst_types) - 1)])  # choix aléatoire des obstacles
    return obst_liste

def obstacles_deplacement(obst_liste):
    """déplacement des obstacles vers la gauche et suppression s'ils sortent du cadre"""
    global obst_types, difficulté
    for obst in obst_liste:

        obst[0] -= int(np.log(difficulté))  # on recule d'un pixel au début puis de plus en plus en suivant une courbe logarithmique pour ne pas monter indéfiniment
        tpobst=obst[1]              # type d'obtacle
        tpdesc= obst_types[tpobst]  # triplet de description du type
        lgobst=tpdesc[0]             # largeur de ce type d'obstacle
        if  (obst[0]+lgobst)<0:         # si la fin de l-objet sort du cadre, on le supprime
            obst_liste.remove(obst)
    return obst_liste

#=======================================================================
# GESTION DES PLATEFORMES (même strucure que les objets)
#=======================================================================
def platforms_creation(plats_liste):
    """création aléatoire de plateformes"""
    global h_debout, ht_plat   
    if pyxel.frame_count % (60/int(np.log(difficulté))) == 0 and random.randint(1, 100) <= 80:
        plats_liste.append([120, random.randint(0+h_debout+40, 90),random.randint(0,2)])
    return plats_liste

def platforms_deplacement(plats_liste):
    """déplacement des plateformes vers la gauche et suppression s'ils sortent du cadre"""
    global difficulté
    for plat in plats_liste:
        plat[0] -= int(np.log(difficulté))              
        if  (plat[0]+lg_plat)<0:           
            plats_liste.remove(plat)
    return plats_liste

# gestion du sol haut généré par les plateformes
def update_sol():
    global plats_liste
    global sol, sol_bas
    global lg_perso             # longueur en X du perso
    global lg_rampe
    global rampe
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
        if rampe:
            if ((perso_x+lg_rampe)>=plat[0]+2) and ((perso_x +2)<(plat[0]+lg_plat)):
                sol=plat[1]                          # alors le sol est defini par cette plateforme
                exist_plat_en_x = True
                plat_en_x = plat
        else:
            if ((perso_x+lg_perso)>=plat[0]+2) and ((perso_x +2)<(plat[0]+lg_plat)):
                sol=plat[1]                          # alors le sol est defini par cette plateforme
                exist_plat_en_x = True
                plat_en_x = plat
    if not exist_plat_en_x:                           # sinon c'est un trou: on tombe
        sol = sol_bas                               # necessite de calculer d'abord sol_bas
    # DEBUG
    #print("exist plat = ", exist_plat_en_x)
    #print("plateforme en X = ", plat_en_x)
    #print("platforme ex x de ", plat_en_x[0]," a ", plat_en_x[0]+lg_plat)
    #print("sol= ",sol)
    #xxx=input("taper une touche pour continuer")
 
 # gestion du sol bas généré par les obstacles et le plancher
def update_sol_bas():
    global obst_liste
    global sol_bas
    global lg_perso             
    global lg_rampe
    global rampe
    global perso_x              
    # on cherche si un obstacle est present au niveau X du perso
    # si oui, on ajuste "sol_bas" à la hauteur du haut de cet obstacle
    exist_obst_en_x = False 
    obst_en_x = [0,0]           # pour debug
    obst=[0,0]                  # pour debug
    for obst in obst_liste:
        # pour chaque obstacle, voir si il est en position du perso
        # pour un meilleur rendu, on enleve quelques pixels de chaque côté à la place occupée par le perso
    
        # pour etre sur l'obstacle ilfaut que le perso morde par sa droite de plus de 2 pixels sur la gauche de la plateforme
        # et que le perso soit encore sur sa gauche sur la plateforme de plus de 2 pixels
        tpobst=obst[1]                  # type d'obtacle
        tpdesc= obst_types[tpobst]      # triplet de description du type
        lgobst=tpdesc[0]                # largeur de ce type d'obstacle
        htobst=tpdesc[1]                # hauteur de ce type d'obstacle
        if rampe:
            if ((perso_x+lg_rampe)>=obst[0]+2) and ((perso_x +2)<(obst[0]+lgobst)):  
                sol_bas=plancher-htobst     # alors le sol-bas est defini par cet obstacle
                exist_obst_en_x = True
                obst_en_x = obst
        else:
            if ((perso_x+lg_perso)>=obst[0]+2) and ((perso_x +2)<(obst[0]+lgobst)):
                sol_bas=plancher-htobst     # alors le sol-bas est defini par cet obstacle
                exist_obst_en_x = True
                obst_en_x = obst
    if not exist_obst_en_x:              # sinon c'est le sol bas normal (plancher)
        sol_bas = plancher

    # DEBUG
    #print("exist obst = ", exist_obst_en_x)
    #print("obstacle en X = ", obst_en_x)
    #print("obstacle en x de ", obst_en_x[0]," a ", obst_en_x[0]+lg_obst)
    #print("sol_bas= ",sol_bas)
    #xxx=input("taper une touche pour continuer")

def pousse_ou_tue():
    global perso_x, perso_y, hauteur_perso, h_rampe, sol, plancher, sol_bas, obst_liste, obst_types, lg_perso, lg_rampe, rampe, mort, difficulté
    # dit si le perso touche un obstacle par sa droite
    # si oui il faufdra décaler le perso en X à gauche de 1 position (comme l'obstacle)
    # gestion des collisions avec obstacles et poussage à gauche
    for obst in obst_liste:
        tpobst=obst[1]                  # type d'obtacle
        tpdesc= obst_types[tpobst]      # triplet de description du type
        htobst=tpdesc[1]                # hauteur de ce type d'obstacle
        mortel = tpdesc[2]              # tue par contact
        if rampe:
            if perso_x+lg_rampe>=obst[0]-1 and perso_x+lg_rampe<=obst[0]+15: # espace pris par l'obstacle
                if mortel and perso_y+hauteur_perso >= 104:
                    mort = True
                elif perso_y+hauteur_perso == plancher:
                    perso_x -= int(np.log(difficulté)) + 1 # on se fait repousser par les obstacles passifs
                    if perso_x < 0:
                        mort = True 
        else:
            if perso_x+lg_perso>=obst[0]-1 and perso_x+lg_rampe<=obst[0]+15: 
                if mortel and perso_y+hauteur_perso >= 104:
                    mort = True
                elif perso_y+hauteur_perso == plancher:
                    perso_x -= int(np.log(difficulté))
                    if perso_x < 0:
                        mort = True 


#========================================================================
# GESTION DU PERSONNAGE
#========================================================================


def perso_deplacement():
    global perso_y, perso_x, sol, saut, rampe, taille_perso, hauteur_perso, h_rampe, h_debout, max_saut, mort

    bas_perso = perso_y+hauteur_perso     # perso_y = le haut de l'image perso, hauteurperso= hauteur de l'image (toujours 16)
    rampe = pyxel.btn(pyxel.KEY_DOWN) and ((bas_perso == sol)or(bas_perso == sol_bas))
    # mise à jour taille max personnage, pour  gestion collisions
    # pour l'affichage on affiche toujeur 16 pix de haut actuellement  ("hauteur_perso")
    if rampe and perso_x <= 65:
        taille_perso = h_rampe  # hauteur utile si rampe
        perso_x += 1
    else:
        taille_perso = h_debout # hauteur utile si debout

    #gestion des sauts (monte en plusieurs fois jusqu'à la hauteur max_saut)
    
    if pyxel.btnp(pyxel.KEY_UP) and ((bas_perso == sol)or(bas_perso == sol_bas)):
        # on ne peut commencer un saut que si on est au sol: plateforme ou bas
        saut = True
        #print(" score = ", score)
    if saut:
        if pyxel.btnp(pyxel.KEY_UP,1,1):    # si la touche fleche est maintenue on continue à sauter
            perso_y -=3
            if perso_y <= max_saut:         # on a depassé la hauteur max (inversé): on retombe au sol
                saut = False
            elif sol<perso_y<sol+ht_plat:       # on etait en train de remonter et on depasse le bas de la plateforme courante
                saut=False
        else:                               # on a arreté d'appuyer sur fleche haut
            saut = False
    else:
        # on retombe ou on reste au sol
        # si on a une platefome, ou aura toujours sol <= sol_bas
        # on teste d'abord la plateforme, puis le sol bas
        if bas_perso<=sol:                                  # on est encore en l'air au dessus d'une plateforme
            perso_y = min(perso_y+3,sol-hauteur_perso)      # on retombe de 3 pixels, ou on touche la plateforme
        else:
            perso_y = min(perso_y+3,sol_bas-hauteur_perso)  # on retombe de 3 pixels, ou on touche le sol ou au dessus d'un obstacle

    # gestion des collisions et poussage
    pousse_ou_tue()


def perso_mort():
    if perso_y+hauteur_perso >= sol:
        mort = False
    else:
        mort = True
        score = 0       #les point+compteur du score seront ajoutés après
        saut = False    #nécessaire?

def menu_mort():
    global mort
    global restart
    # si le personnage est mort, on attend un "return"
    if mort and pyxel.btnp(pyxel.KEY_RETURN):
        mort = False
        restart=True
    


#===================================================================================
# fonction à appeler dans la fonction "update" du module principal si ingame==True
#===================================================================================       
def game_update():                  #fonction de calcul periodique
    global plats_liste
    global obst_liste
    global mort
    global restart
    global difficulté
    global score
    global count


    # creation des plateformes
    plats_liste = platforms_creation(plats_liste)
    # mise a jour des positions des plateformes
    plats_liste = platforms_deplacement(plats_liste)

    # creation des obstacles
    obst_liste = obstacles_creation(obst_liste)
    # mise a jour des positions des obstacles
    obst_liste = obstacles_deplacement(obst_liste)
    
    # incrémentation de la difficulté et calcul du score
    count += 1
    if count % 5 == 0:
        # augmentation progressive de la difficulté qui sera exprimé par une augmentation de forme logarithmique de la vitesse du scrolling
        difficulté += 1/20
    if count % 1 == 0:
        # augmentation du score
        score += int(1*np.e**((difficulté-np.e)/10))  # contrairement à la vitesse du scrolling, le score augmante de manière expo

    update_sol_bas()        # a faire avant update_sol
    update_sol()            # necessite sol_bas
    perso_deplacement()

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
    global perso_x
    global perso_y
    global plats_liste
    global obst_liste
    global obst_types
    global rampe
    global plancher
    global score

    pyxel.load("menus.pyxres")              # fichier ressources à renommer si besoin

    pyxel.bltm(0,0,0,0,128,128,128) 
    pyxel.mouse(False)                   # rendre le curseur in visible

    if mort:
        pyxel.cls(0)
        pyxel.text(20, 50, "Mort, appuie sur return ", 7)
        # print("mort main loop")

  
    else:
        pyxel.load("res.pyxres")
        # vide la fenetre
        #pyxel.cls(0)

        # sol
        pyxel.rect(0,124,128,4,4)
        # a remplacer par une succession de dessins pyxres qui defilent
        # au meme rythme que les obstacles
        
        # plateformes
        for plat in plats_liste:
            pyxel.blt(plat[0],plat[1],1,0,52+plat[2]*16,lg_plat,ht_plat,2)
            #pyxel.rect(plat[0], plat[1], lg_plat, ht_plat, 4)  # a remplacer par dessin pyxres

        # obstacles au sol
        for obst in obst_liste:
            tpobst=obst[1]                  # type d'obtacle
            tpdesc= obst_types[tpobst]      # triplet de description du type
            lgobst=tpdesc[0]                # largeur de ce type d'obstacle
            htobst=tpdesc[1]                # hauteur de ce type d'obstacle
            xobst = tpdesc[3]                 # coord X du dessin dans res.pyxres
            yobst = tpdesc[4]                 # coord Y du dessin dans res.pyxres
                        
            # pyxel.rect(obst[0],,lgobst,htobst,6)
            pyxel.blt(obst[0],plancher-htobst,1,xobst,yobst,lgobst,htobst,2)
            
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


        pyxel.text(1, 10, str(score), 10) # le score qui s'affiche en haut à gauche de l'écran
