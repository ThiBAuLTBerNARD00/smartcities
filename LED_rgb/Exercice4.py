from ws2812 import WS2812
from machine import I2C,Pin,ADC
import utime
import random

BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,150,0)
GREEN = (0,255,0)
CYAN = (0,255,255)
BLUE = (0,0,255)
PURPLE = (180,0,255)
WITHE = (255,255,255)

COLORS = (BLACK,RED,YELLOW,GREEN,CYAN,BLUE,PURPLE,WITHE)

led = WS2812(18,1)#pin and led count
Light_sensor = ADC(0)
Sound_sensor = ADC(1)

def detect_sound():
    noise = 0
    average = 0
    for i in range (1000):
        noise = Sound_sensor.read_u16()/256
        average += noise
    noise = int(average/1000)
    print("noise",noise)
    return noise

def detect_Pic(moyenne):
    noise = 0
    average = 0
    print("moyenne",moyenne)
    for i in range (10):
        noise = Sound_sensor.read_u16()/256
        average += noise
    
    son= int(average/10)  
    print(son)
    if son > (moyenne+10):
        led.pixels_fill(random.choice(COLORS))
        led.pixels_show()
        utime.sleep(1)
    

while True:
    
    ligth =Light_sensor.read_u16()/256
    #noise = Sound_sensor.read_u16()/256
    moyenne  = detect_sound()
    utime.sleep(1)
    detect_Pic(moyenne)
    
    #if ligth <80:
        #led.pixels_fill(WITHE)
        #led.pixels_show()
        #utime.sleep(0.1)
    #else:
        #if noise != noise1 and noise>average1+10:
            #led.pixels_fill(random.choice(COLORS))
            #led.pixels_show()
            #utime.sleep(1)
        #if noise > 35 and noise <50:
        #    led.pixels_fill(YELLOW)
        #    led.pixels_show()
        #    utime.sleep(1)
        #if noise <35:
        #    led.pixels_fill(GREEN)
        #    led.pixels_show()
        #    utime.sleep(1)
        #if noise >55:
        #    led.pixels_fill(RED)
        #    led.pixels_show()
        #    utime.sleep(1)
        #led.rainbow_cycle(0)
