import machine
from machine import Pin
from time import sleep

# Définition des pins pour la LED et le bouton poussoir
button = Pin(16, Pin.IN)
led = Pin(18, Pin.OUT)

# Initialisation des variables
val = 0
blink_speed = 1  # Fréquence par défaut (0.5 Hz)

# Fonction appelée à chaque pression du bouton
def bouton_presse(pin):
    global val
    val += 1
    if val > 2:  # Réinitialisation après la 3e pression
        val = 0
    print("Bouton pressé, val =", val)

# Attachement de l'interruption à la pression du bouton
button.irq(trigger=Pin.IRQ_FALLING, handler=bouton_presse)

def Sequence_clignotement(temps):
        led.value(1)
        sleep(temps)  # 1 seconde allumée
        led.value(0)
        sleep(temps)  # 1 seconde éteinte (clignotement à 0.5 Hz)

while True:
    if val == 0:  # Si le bouton a été pressé 3 fois (LED éteinte)
        led.value(0)
    elif val == 1:  # Si le bouton a été pressé 1 fois (clignotement lent)
        Sequence_clignotement(1) # 1 seconde éteinte (clignotement à 0.5 Hz)
    elif val == 2:  # Si le bouton a été pressé 2 fois (clignotement rapide)
        Sequence_clignotement(0.3) # 0.3 seconde éteinte (clignotement plus rapide)
