from ws2812 import WS2812
from machine import I2C,Pin,ADC
import utime


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

while True:
    average =0
    ligth =Light_sensor.read_u16()/256
    #noise = Sound_sensor.read_u16()/256
    
    for i in range (1000):
        noise = Sound_sensor.read_u16()/256
        average += noise
    noise = average/1000
    print(noise)
    if ligth <80:
        led.pixels_fill(WITHE)
        led.pixels_show()
        utime.sleep(0.1)
    else:
        
        if noise > 25 and noise <50:
            led.pixels_fill(YELLOW)
            led.pixels_show()
            utime.sleep(1)
        if noise <25:
            led.pixels_fill(GREEN)
            led.pixels_show()
            utime.sleep(1)
        if noise >50:
            led.pixels_fill(RED)
            led.pixels_show()
            utime.sleep(1)
