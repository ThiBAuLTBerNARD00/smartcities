# Projet Smartcities

## Contexte
Dans le cadre du cours de **SmartCities & IoT**, je dois réaliser différents petits projets ayant pour objectif l'apprentissage de la programmation embarquée en MicroPython. Chaque projet se concentre sur un aspect spécifique, qu'il s'agisse de l'emploi de méthodes de programmation différentes ou de l'utilisation de divers composants tels que des moteurs, des buzzers, des potentiomètres, etc.

Ces projets seront réalisés à l'aide d'un kit de base **Grove** et d'un **Raspberry Pico W**.

## Répertoires
- **GPIO** : Gestion des entrées/sorties numériques
- **AD-PWM** : Contrôle des signaux analogiques et modulation de largeur d'impulsion
- **LCD** : Utilisation d'un écran LCD pour afficher des informations
- **LED-neo** : Contrôle des LED Neopixel
- **Network** : Fonctionnalités réseau (WiFi/Bluetooth)
- **Sensors** : Interface avec divers capteurs

## Raspberry Pico W
Les **Raspberry Pico** sont des microcontrôleurs performants, ultra-légers et compacts, ce qui en fait une solution idéale pour des projets de systèmes embarqués. Le **Raspberry Pico W** est une version qui intègre une carte réseau, ajoutant des capacités WiFi et Bluetooth à la programmation sur microcontrôleur.

### Pinout
![Pinout du Raspberry Pico W](https://github.com/hepl-scheen/smartcities/assets/158835010/20d19fc4-b9c3-4903-9ec8-b62cda90aee3)

## MicroPython
![Logo MicroPython](https://en.wikipedia.org/wiki/MicroPython#/media/File:MicroPython_new_logo.svg)

**MicroPython** est une implémentation du langage Python 3, optimisée pour fonctionner sur des microcontrôleurs. Elle inclut une partie des bibliothèques standards de Python et propose des modules spécifiques pour exploiter les fonctionnalités matérielles embarquées telles que :
- GPIO
- Timers
- ADC (convertisseur analogique-numérique)
- PWM (modulation de largeur d'impulsion)
- SPI, I²C, CAN, Bluetooth, USB

Dans le cadre de ce cours, j'utiliserai un **Raspberry Pico**, mais d'autres microcontrôleurs comme les séries **ESP32**, **ESP8266** et les **Arduino UNO** peuvent aussi être programmés en MicroPython.

## Visual Studio Code
![Logo Visual Studio Code](https://code.visualstudio.com/assets/images/code-stable.png)

**Visual Studio Code** est un IDE léger et polyvalent, supportant une grande variété de langages de programmation. Grâce à une communauté active, VSCode dispose d'une immense bibliothèque d'extensions, le rendant extrêmement flexible selon les besoins de chaque programmeur.

## MicroPico
L'extension **MicroPico Visual Studio Code**, développée par [paulober](https://github.com/paulober), permet de simplifier et d'accélérer le développement des projets MicroPython sur Raspberry Pi Pico et Pico W. Cette extension propose notamment :
- Highlighting et auto-complétion pour MicroPython
- Snippets de code
- Intégration au terminal pour communiquer avec le Raspberry Pico

---

*Projet réalisé dans le cadre du cours SmartCities & IoT - MicroPython sur Raspberry Pico W.*
