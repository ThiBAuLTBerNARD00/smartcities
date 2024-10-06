from lcd1602 import LCD1602
from dht11 import *
from machine import I2C,Pin,ADC,PWM,Timer
from utime import sleep
import _thread

i2c = I2C(1,scl=Pin(7),sda = Pin(6), freq=400000)
d= LCD1602(i2c,2,16)

d.display()
dht = DHT(18)
buzzer = PWM(Pin(16))
Rotary_angle_sensor = ADC(0)
led = Pin(20, Pin.OUT)
SetTemp=0
def ReadADC(timer):
    global Rotary_angle_sensor
    global SetTemp
    vol = Rotary_angle_sensor.read_u16()
    SetTemp = int(vol/65535*20)+15
    global temp
    #print("Valeur de temps:",temp)
    #Test_Temp(temp,SetTemp)
    
tim = Timer()   
tim.init(mode=Timer.PERIODIC, freq=150, callback=ReadADC)

def RunAlram(force):
    if  force==True:
        buzzer.freq(1000)
        buzzer.duty_u16(200) # a augmenter, momentanément baisser pour les tests
    else :
        buzzer.duty_u16(0)
def Sequence_clignotement(temps):
        led.value(1)
        sleep(temps)  # 1 seconde allumée
        led.value(0)
        sleep(temps)  # 1 seconde éteinte (clignotement à 0.5 Hz)
def Test_Temp(temp,SetTemp):
    if temp>SetTemp:          
          if temp-SetTemp>3:
               #t =threading.Thread(target=Sequence_clignotement,args=(1,))
               #t.start()
               _thread.start_new_thread(Sequence_clignotement,(0.1,))
               RunAlram(True)
               for i in 0,10:
                    #Sequence_clignotement(0.1)
                    d.clear()
                    d.setCursor(i,0)
                    d.print("ALARM")
                    sleep(0.8)
                #t.join()
          else:
               RunAlram(False)
               Sequence_clignotement(1.5)
          
    else:
        RunAlram(False)
        
               
          

while True:
    temp,humid = dht.readTempHumid()
    d.clear()
    d.setCursor(0,0)
    d.print("Ambient:"+str(temp))
    d.setCursor(0,1)
    d.print("SetTemp:"+str(SetTemp))
    Test_Temp(temp,SetTemp)
    #sleep(1)