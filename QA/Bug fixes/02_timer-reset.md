# Rapport de bug - Alignement caméra

Date : 06/05  
Statut : Résolu  
Méthode de test : Test exploratoire

#### Description  
Lors d'une deuxième partie, le temps restant lors de la dernière session est conservé et appliqué

#### Étapes pour reproduire 
1. Compléter une première partie
2. Retourner au menu et commencer une nouvelle partie


#### Comportement attendu  
Le timer est réinitialisé, donnant le temps nécessaire au joueur pour compléter le niveau.

#### Comportement observé  
Le temps restant de la partie précédante est conservé.
Si le temps était écoulé, la partie commence directement au niveau 2.

#### Analyse 
A la fin de la partie, le timer n'est pas réitialisé.

#### Résolution  
Réinitialisation de la valeur **time_left** :

main.py : 

    def handle_endscreen(self, event):
        ...
        self.time_passed = 0
        self.time_left = 90.0
