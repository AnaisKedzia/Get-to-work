# Rapport de bug - Alignement caméra

Date : 03/03  
Statut : Résolu  
Méthode de test : Test fonctionnel

#### Description  
La caméra ne s'aligne pas correctement avec les limites de la carte. Ce problème survient 
après une collision entre joueur et ennemi.

#### Étapes pour reproduire 
1. Entrer en collision avec un ennemi
2. Se libérer et aller en bord de carte pour constater l'erreur (début ou fin)


#### Comportement attendu  
L'alignement de la caméra avec la carte reste cohérent et juste.

#### Comportement observé  
Un décallage carte / caméra se produit, rendant visible l'espace au delà des limites de carte, ou
empêchant une transition fluide entre les sections.

#### Analyse 
Dans la fonction camera_shake qui vise à créer un effet caméra lorsque le joueur est attrapé, une valeur clé n'est pas réitialisée.

#### Résolution  
Réitialiser la valeur **effect_t** à la fin de l'effet.

*Code initial* :

    def shake(self):
        if self.shaking == True and self.effect_t < 5 :
            self.x += 10 + (- 20 * (self.effect_t % 2))
            self.effect_t += 1
        else : 
            self.shaking = False

*Code mofidié* :

    def shake(self):
        if self.shaking == True and self.effect_t < 5 :
            self.x += 10 + (- 20 * (self.effect_t % 2))
            self.effect_t += 1
        else : 
            self.shaking = False
            self.effect_t = 1

