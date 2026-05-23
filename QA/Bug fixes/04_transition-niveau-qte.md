# Rapport de bug - Transition niveau QTE

Date : 19/05  
Statut : Résolu  
Méthode de test : TC-10

#### Description  
Le QTE persiste après la transition au niveau suivant.

#### Étapes pour reproduire 
1. Entrer en collision avec un ennemi
2. Attendre l'écoulement du timer


#### Comportement attendu  
Le prochain niveau se charge et le joueur peut se déplacer librement

#### Comportement observé  
Le prochain niveau se charge, mais le QTE déclenché lors du dernier niveau reste actif. L'animation du joueur affiche l'animation "caught" avec l'ennemi du niveau actuel. Il est toujours possible de compléter le QTE et de reprendre la partie. 

#### Analyse 
Lorsqu'une collision ennemie est détectée, l'état du jeu devient "QTE", et n'est pas réinitialisée à "PLAYING" lorsque le timer se termine. 

#### Résolution  
Réinitialisation de l'état, désactivation du QTE et déblocage du joueur.  

*Code initial* :

main.py : 

    def run(self): 

                ...

                self.time_left -= dt
                if self.time_left < 0:
                    self.next_level()


*Code modifié* : 

main.py :

    def run(self) :

                ...

                self.time_left -= dt
                if self.time_left < 0:
                    self.qte.active = False
                    self.GAME_STATE = "PLAYING"
                    self.player.unlock()
                    self.next_level()
