import machine
from machine import Pin

from time import sleep
val = 0
Button = machine.Pin(16, machine.Pin.IN)

LED = machine.Pin(18, machine.Pin.OUT)

littel = False
greater = False
def bouton_presse(pin):
    print("bouton pressé")
    global val
    val = val + 1
    print("val",val)
    if val !=1:
        littel = False
    
Button.irq(trigger=Pin.IRQ_FALLING,handler=bouton_presse)

LED.value(1)

x=1
while val <3:
    print(val)
    if (val == 1 or littel == True) and val<=1:
        if littel != True:
            val =0            
            littel = True
            greater = False
            x=1
        LED.value(1)
        sleep(1)
    else:
        littel = False
        if val == 2 or greater == True:
            print("valeur de greater" , greater)
            if greater != True:
                val=0
                x=0.3
            littel = False
            greater =True
            val =0
            LED.value(1)
            sleep(0.3)
    LED.value(0)
    sleep(x)
val=0  

            
  
  
  
 
