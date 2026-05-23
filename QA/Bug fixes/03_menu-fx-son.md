# Rapport de bug - Menu FX son

Date : 06/05  
Statut : Résolu  
Méthode de test : Test exploratoire

#### Description  
Lors du retour au menu après une première partie, les sons accompagnant l'affichage du titre ne se déclenchent pas.

#### Étapes pour reproduire 
1. Compléter une première partie
2. Retourner au menu


#### Comportement attendu  
Le titre s'affiche en plusieurs fois, chaque bout de titre accompagné de son effet sonore.

#### Comportement observé  
Le titre s'affiche en plusieurs fois mais en silence.

#### Analyse 
Dans menu.py, une expression booléenne détermine si le son a déjà été joué. Lors du retour au menu, l'expression est égale à True et le son ne se joue pas.

#### Résolution  
Réinitialisation des expressions. Deux solutions sont possibles :

1 - Réinitialiser le menu 

Réinitialiser le menu en créant une nouvelle instance de Menu :

main.py


    self.menu = Menu()


Cette approche est simple et réinitialise les expressions à leur valeur d'orgine False. L'inconvénient est qu'il réinitialise aussi l'affichage des cinématiques. Le système ne se souvient pas du choix initial et le joueur doit désactiver les animations sur le menu à chaque nouvelle partie.

2 - Réinitialiser directement les valeurs booléennes avec une loupe : 

main.py

    def handle_endscreen(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e :
                for i in range(len(self.menu.title)):
                    self.menu.title[i][3] = False

La seconde approche est sélectionnée pour assurer la persistance des autres éléments. 