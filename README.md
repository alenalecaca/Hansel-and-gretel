# Hansel-and-gretel
Readme V2 du 2 Mai 2024.

creer par: Alena Pogudina, Elise Schultz, Alienor Rousseau, Rafael Martellini

inspiration : conte de Hansel and Gretel ; frères Grimm

histoire : "Hansel et Gretel" est un conte populaire allemand des frères Grimm. Il raconte l'histoire de deux enfants abandonnés dans la forêt par leur méchante belle-mère, qui trouvent une maison en pain d'épice appartenant à une sorcière. Ils parviennent à échapper à ses griffes et retournent chez eux avec des trésors.

-----------------------------------------------------------------------
description du jeu :  
Le jeu Hansel & Gretel sera un jeu de plateformes qui sera basé sur le conte des frères Grimm. Le personnage se "déplacera" sur un sol mais pourra aussi survoler les obstacles bloquant le chemin grâce à des plateformes flottantes. Le personnage, "poursuivi" par la sorcière, devra éviter les obstacles qui le feront reculer, ou pour certains le tueront. L'objectif n'est pas de "gagner" mais de tenir le plus longtemps possible avec un grand nombre de sauts.
-----------------------------------------------------------------------
Questions  
1 - Interface graphique et bibliothèque graphique : Le jeu vidéo "Hansel and Gretel" utilisera l'interface graphique fournie par le site Pixel Studio. La bibliothèque graphique associée à Pixel Studio sera utilisée pour le développement visuel du jeu.  
2 - Interaction utilisateur : Les interactions pendant le jeu se feront via le clavier. Les menus principaux du jeu seront, eux, contrôlés à la souris. pour cela, la partie menus et la partie jeu seront bien séparées.Le jeu est conçu pour un seul utilisateur.  
3 - Partie audio : Le jeu comportera des éléments audio tels que musiques d'ambiance, effets sonores et bruitages. Ces éléments audio seront créés en interne pour assurer une intégration harmonieuse avec le jeu.  
4 - Présence de menus : Un écran de menus apparait au début du jeu. l'interaction se fait avec la souris. Avant le début du jeu, les utilisateurs pourront accéder à ce menu permettant de consulter le manuel du jeu, fournissant des informations sur les touches de contrôle et d'autres conseils utiles.  
5 - Paramètres réglables par l'utilisateur : La difficulté du jeu évoluera progressivement en fonction du score atteint dans la partie courante. Cela se traduira principalement par une augmentation de la vitesse du jeu.  
6 - Évolutivité durant l'utilisation : Le jeu n'est pas conçu avec des niveaux définis, mais avec des parties infinies et génerées de pmanière aléatoire. La difficulté augmentera au fil de la progression du jeu, jusqu'à rester à un niveau stagnant ( la programmation de la difficulté est basée sur la fonction exponentielle ).   
7 - Programmation complexe : Une intelligence artificielle (IA) sera implémentée pour contrôler les déplacements de la sorcière. La sorcière se déplacera de manière aléatoire, mais conformément à des conditions prédéfinies pour assurer un défi constant aux joueurs.(pas encore implémenté)  
8 - Quel sera le format des fichiers audio utilisés dans le jeu ? Le format des fichiers audio utilisés dans le jeu sera déterminé ultérieurement, en fonction des besoins spécifiques en termes de qualité sonore et de compatibilité avec la plateforme de déploiement. (pas encore implémenté)  
9 - Comment seront gérées les sauvegardes de progression des joueurs ? Les sauvegardes de progression des joueurs ne sont pas propoées. Le jeu est instantané pour chaque partie. On peut faire une pause dans le jeu mais pas sauvegarder une partie.  
10 -  a-t-il des exigences particulières en matière de performances ou de compatibilité avec les systèmes d'exploitation ? Aucune exigence particulière en matière de performances n'est spécifiée, et le jeu sera compatible avec les systèmes d'exploitation pris en charge par la plateforme GitHub et Pyxel.  
-----------------------------------------------------------------------
Commentaires sur le cahier des charges :
- Si vous pensez faire un menu avec un bouton ("trois traits") accessible pendant le jeu, cela suppose l'utilisation de la souris, en plus du clavier.
- Si vous prenez la peine d'avoir le choix entre 2 personnages, il faut que cela change quelque chose dans le jeu. Sinon, laissez tomber.
- Programmer un déplacement aléatoire de la sorcière n'est pas forcément chose facile, surtout s'il y a des obstacles à gérer.
- Vos points 8 à 10 n'ont pas de sens dans le cadre de ce projet puisque vous avez choisi de passer par Pixel.
-----------------------------------------------------------------------
Commentaires sur le planning :
Le planning doit aller jusqu'à la fin du projet, c'est-à-dire le 19 avril.
Les tâches sont trop vagues et/ou trop grosses. Par exemple "developper la boutique et linformations disponible dans le menu" ne me paraît pas faisable pour une seule personne en 2h.
Tel que vous l'avez écrit, le jeu serait presque terminé d'ici un mois, cela ne me semble pas très réaliste. Et la tâche "programmer le personnage qui saute et comment il va depacer les obstacles" semble être la seule qui concerne le déplacement du personnage principal du jeu. Or elle vient à la fin alors que déplacer le personnage est une des premières choses à faire.
La répartition ne me semble pas très adaptée. La programmation des déplacements de la sorcière est une tâche compliquée qui devrait aller aux personnes les plus à l'aise en programmation.
