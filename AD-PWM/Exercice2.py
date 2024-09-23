from machine import Pin,PWM,ADC,Timer
from time import sleep

Rotary_angle_sensor = ADC(0)

buzzer = PWM(Pin(27))
vol = 200
vol = Rotary_angle_sensor.read_u16()
def ReadADC(timer):
    global vol
    global Rotary_angle_sensor
    vol = Rotary_angle_sensor.read_u16()
    vol = int(vol/65535*9000)
    print(vol)


tim = Timer()   
tim.init(mode=Timer.PERIODIC, freq=100, callback=ReadADC)

def DO(time):
        #DO
    buzzer.freq(1046)
    buzzer.duty_u16(vol)
    sleep(time)
def RE(time):
        #RE
    buzzer.freq(1175)
    buzzer.duty_u16(vol)
    sleep(time)
def MI(time):
        #MI
    buzzer.freq(1318)
    buzzer.duty_u16(vol)
    sleep(time)
def FA(time):
        #FA
    buzzer.freq(1397)
    buzzer.duty_u16(vol)
    sleep(time)
def SO(time):
        #SO
    buzzer.freq(1568)
    buzzer.duty_u16(vol)
    sleep(time)
def LA(time):
        #LA
    buzzer.freq(1760)
    buzzer.duty_u16(vol)
    sleep(time)
def SI(time):
        #SI
    buzzer.freq(1967)
    buzzer.duty_u16(vol)
    sleep(time)

def PremierMelodie():
    DO(1)
    RE(1)
    MI(1)
    FA(1)
    SO(1)
    LA(1)
    SI(1)

#def SecondeMelodie():

while True:
    print(vol)
    PremierMelodie()


