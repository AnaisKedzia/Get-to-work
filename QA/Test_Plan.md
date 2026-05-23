# Plan de test - GET TO WORK
Date : 18/05/26  
Auteur : Anaïs Kedzia

## Objectif  
Vérifier le fonctionnement des commandes principales du jeu et le bon déroulement d'une partie complète.

## Périmètre
- Mouvements latéraux et sauts
- Collisions obstacles
- Rencontre ennemis
- Collecte d'items
- Complétion des niveaux / d'une partie complète
- Tests de limites (carte, temps)
- QTE

## Hors-périmètre
- Performance
- Compatabilité multi-OS

## Techniques
- Tests fonctionnels
- Test exploratoires
- Test boîte noire

## Risques identifiés
- Dysfonctionnement du timer
- Entrées multiples
- Détection erronée des collisions
- Blocage lors des transitions caméras
- Réiniatialisation incomplète des éléments à la fin d'une partie

## Environnement et outils
- OS : Window
- IDE : Visual Studio Code
- Language : Python 3.13
- Bibliothèque : Pygame