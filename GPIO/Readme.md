# Projet LED Clignotante avec Bouton Poussoir

## Contexte
Ce projet utilise un **Raspberry Pi Pico** avec MicroPython pour contrôler une LED et un bouton poussoir. La LED clignote à différentes vitesses en fonction du nombre de fois où le bouton est pressé. Après trois pressions, la séquence de clignotement se réinitialise.

## Fonctionnalités
- **Pression du bouton** : Le bouton poussoir déclenche un changement de comportement à chaque pression (cycle de 3 états).
- **Clignotement de la LED** : La LED clignote lentement ou rapidement en fonction du nombre de pressions :
  - **0 pressions** : LED éteinte.
  - **1 pression** : Clignotement lent (1 seconde allumée, 1 seconde éteinte).
  - **2 pressions** : Clignotement rapide (0.3 seconde allumée, 0.3 seconde éteinte).
  - **3 pressions** : Réinitialisation à l'état éteint.

## Schéma de câblage
- **Pin 16** : Bouton poussoir
- **Pin 18** : LED

## Flowchart

```mermaid
graph TD;
    Start[Début] --> B[Attente d'une pression du bouton];
    B -->|0 pressions| D[LED éteinte];
    B -->|1 pression| E[Clignotement lent (1 Hz)];
    B -->|2 pressions| F[Clignotement rapide (3.33 Hz)];
    B -->|3 pressions| G[Réinitialisation];
    G --> B;
    E --> B;
    F --> B;
    D --> B;

