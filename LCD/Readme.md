# Système de Surveillance de Température avec Alarme

## Description
Ce projet utilise un **Raspberry Pi Pico** pour surveiller la température ambiante à l'aide d'un capteur **DHT11**. La température de consigne est définie via un **capteur rotatif**. Si la température ambiante dépasse la température de consigne, un système d'alarme se déclenche : un **buzzer** sonne et une **LED** clignote. L'écran **LCD1602** affiche en temps réel la température actuelle et la température de consigne.

## Fonctionnalités
- **Capteur de température DHT11** : Mesure la température et l'humidité ambiantes.
- **Capteur rotatif** : Permet de régler la température de consigne entre 15°C et 35°C.
- **Alarme (buzzer et LED)** : Se déclenche si la température ambiante dépasse la température de consigne de plus de 3°C.
- **Écran LCD1602** : Affiche la température ambiante et la température de consigne.
- **Multithreading** : La LED clignote en parallèle via l’utilisation de threads.

## Matériel utilisé
- **Raspberry Pi Pico**
- **Capteur DHT11** (mesure de la température et de l'humidité)
- **Capteur rotatif** (réglage de la température)
- **Buzzer** (pour l'alarme sonore)
- **LED** (pour l'alarme visuelle)
- **Écran LCD1602** (pour l'affichage des températures)
- **Threading** (pour gérer le clignotement de la LED de manière indépendante)

## Fonctionnement du système
1. **Lecture des données de température** : Le capteur **DHT11** mesure la température ambiante à intervalles réguliers.
2. **Réglage de la température de consigne** : Le capteur rotatif est utilisé pour ajuster la température de consigne affichée sur l'écran LCD.
3. **Détection des écarts de température** :
   - Si la température ambiante dépasse la température de consigne de plus de 3°C, une alarme sonore (buzzer) et visuelle (LED clignotante) se déclenchent.
   - Si l’écart est inférieur à 3°C, la LED clignote plus lentement et le buzzer est éteint.
4. **Affichage sur l'écran LCD** : La température ambiante et la température de consigne sont affichées en temps réel sur l'écran **LCD1602**.

## Schéma de câblage
- **Pin 7, 6** : Écran LCD1602 (I2C)
- **Pin 18** : Capteur DHT11
- **Pin 0** : Capteur rotatif (ADC)
- **Pin 16** : Buzzer (PWM)
- **Pin 20** : LED (Sortie numérique)

## Flowchart

```mermaid
graph TD;
    Start[Début] --> ReadTemperature[Lecture du capteur DHT11];
    ReadTemperature --> Display[Afficher Température et Consigne sur LCD];
    Display --> ReadRotarySensor[Lecture du capteur rotatif];
    ReadRotarySensor --> SetTemp[Définir la Température de Consigne];
    SetTemp --> Compare[Comparer la Température];
    
    Compare -->|Temp > Consigne + 3°C| TriggerAlarm[Déclencher Alarme et Clignotement];
    Compare -->|Temp <= Consigne + 3°C| NormalState[Alarme Désactivée];
    
    TriggerAlarm --> UpdateLCD[Mise à jour de l'écran LCD avec "ALARM"];
    NormalState --> UpdateLCD[Mise à jour de l'écran LCD avec Température et Consigne];
    
    UpdateLCD --> Loop[Attendre et Répéter];
    Loop --> ReadTemperature;

