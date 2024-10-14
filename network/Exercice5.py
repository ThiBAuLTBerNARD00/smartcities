from machine import Pin,PWM
from utime import sleep
from servo import SERVO
import network
import ntptime
import time
servo = SERVO(Pin(20))
miniPir = Pin(18,Pin.IN)
a=150

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid='Mon gsm'
password = 
wlan.connect(ssid,password)
print(time.localtime())
ntptime.settime()
servo.turn(0)
sleep(1)
while True:
    # if miniPir.value()==1:
    #     print('Motion detected')
    #     servo.turn(150)
    #     sleep(5)
    #     servo.turn(0)
    #     print('remise a zéro')
    #     sleep(2)
    # a=a==0 and 150 or a-1
    # servo.turn(a)
    # sleep(0.1)
    
    print ("Year   = ", time.localtime()[0])
    print ("Month  = ", time.localtime()[1])
    print ("Day    = ", time.localtime()[2])
    hour = time.localtime()[3]
    hour = hour + 2
    print ("Hour   = ", hour)
    print ("Minute = ", time.localtime()[4])
    print ("===============")
    if ((150/12)*hour+(150/(60*12))*time.localtime()[4])<150:
        servo.turn((150/12)*hour+(150/(60*12))*time.localtime()[4])
    else:
        hour = hour -12
        servo.turn((150/12)*hour+(150/(60*12))*time.localtime()[4])
    time.sleep(10)