| ID    |  Titre         | Etapes                                 | Résultat attendu |
| ----- |  ------------- | -------------------------------------- |--------------- |
| TC-01 | Déplacements | 1. Appuyer sur "D" et/ou la flèche directionnielle droite 2. Appuyer sur "Q" et/ou la flèche directionnielle gauche 3. Appuyer sur espace | Le joueur bouge à droite, à gauche, puis saute sur place.  | |
| TC-02 | Collisions | 1. Se déplacer à droite jusqu'à la rencontre d'un obstable 2. Se déplacer sous une plateforme et sauter 3. Sauter sur l'angle d'un bloc (collision horizontale + verticale)| Le mouvement du joueur est stoppé lors de la collision, et ses déplacements sont cohérents | |
| TC-03 | Limites carte | 1. Se déplacer à gauche jusqu'au début d'un niveau 2. Se déplacer à droite jusqu'à la fin du niveau | Le mouvement du joueur est stoppé et la caméra reste fixe | |
| TC-04 | Transitions caméra | 1. Se déplacer à droite jusqu'à la fin de l'écran pour déclencher une transition caméra 2. Se déplacer à gauche pour déclencher de nouveau une transition 3. Répéter 2-3 fois | La caméra se déplace pour afficher la partie ou se trouve le joueur, le joueur est bloqué durant la transition | |
| TC-05 | Collecte d'items | 1. Atteindre l'emplacement d'un item 2. Répéter 2-3 fois | L'item disparaît, un effet sonore se joue et le compteur de l'item se met à jour| |
| TC-06 | Collision ennemi | 1. Atteindre l'emplacement d'un ennemi  | Le joueur est bloqué lors de la collision, l'animation correcte est jouée et un QTE se lance| |
| TC-07 | QTE réussi | 1. Atteindre l'emplacement d'un ennemi 2. Compléter le QTE | Le joueur et l'ennemi reprennent leurs animations de base et le joueur est débloqué| |
| TC-08 | QTE raté | 1. Atteindre l'emplacement d'un ennemi pour lancer le QTE 2. Presser les bons boutons 2 fois 3. Presser le mauvais bouton | A chaque réussite le curseur avance pour indiquer la touche à presser, lors d'une erreur, le curseur réapparaît au début| |
| TC-09 | Immunité | 1. Atteindre l'emplacement d'un ennemi pour lancer le QTE 2. Réussir le QTE 3. Retourner sur l'emplacement de l'ennemi| Le joueur bénéficie d'un laps de temps de 2 secondes qui empêche les collisions ennemis et le déclenchement du QTE, le joueur est de nouveau bloqué après ce laps de temps| |
| TC-10 | Limite de temps QTE | 1. Atteindre l'emplacement d'un ennemi 2 Attendre la fin du chronomètre| La transition QTE -> PLAYING est réussie et le niveau suivant se lance| |
| TC-11 | Désactivation cinématiques| 1. Désactiver les cinématiques dans le menu 2. Lancer une partie | Le gameplay commence directement, sans cinématiques.
| TC-12 | Écran de fin | 1. Compléter une partie pour atteindre l'écran de fin |  Les barres de score s'affichent successivement et correctement, le résultat est communiqué et le retour au menu possible.
| TC-13 | Affichage des commandes | 1. Appuer sur "A" au menu 2. Relâcher "A" |  Les commandes s'affichent lors de l'appui, et disparaissent au relâchement.




