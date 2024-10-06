from machine import Pin,PWM,ADC,Timer
from time import sleep

Rotary_angle_sensor = ADC(0)
button = Pin(16, Pin.IN)
buzzer = PWM(Pin(27))

vol = Rotary_angle_sensor.read_u16()/65535*9000
def ReadADC(timer):
    global vol
    global Rotary_angle_sensor
    vol = Rotary_angle_sensor.read_u16()
    vol = int(vol/65535*9000)
    #print(vol)
song = False
# Fonction appelée à chaque pression du bouton
def bouton_presse(pin):
    print("bouton presse")
    global song
    if song == False:
        song =True
        raise Exception("val song change")
    else:
        song = False
        raise Exception("val song change")

# Attachement de l'interruption à la pression du bouton
button.irq(trigger=Pin.IRQ_FALLING, handler=bouton_presse)

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
    try:
        DO(1)
        RE(1)
        MI(1)
        FA(1)
        SO(1)
        LA(1)
        SI(1)
    except:
        return
    

def playtone(frequency):
    buzzer.duty_u16(vol)
    buzzer.freq(frequency)

def be_quiet():
    buzzer.duty_u16(0)  # turns sound off
def duration(tempo, t):
    
    # calculate the duration of a whole note in milliseconds (60s/tempo)*4 beats
    wholenote = (60000 / tempo) * 4
    
    # calculate the duration of the current note
    # (we need an integer without decimals, hence the // instead of /)
    if t > 0:
      noteDuration = wholenote // t
    elif (t < 0):
      # dotted notes are represented with negative durations
      noteDuration = wholenote // abs(t)
      noteDuration *= 1.5 # increase their duration by a half
    
    return noteDuration
notes = {
"NOTE_B0": 31,
"NOTE_C1": 33,
"NOTE_CS1": 35,
"NOTE_D1": 37,
"NOTE_DS1": 39,
"NOTE_E1": 41,
"NOTE_F1": 44,
"NOTE_FS1": 46,
"NOTE_G1": 49,
"NOTE_GS1": 52,
"NOTE_A1": 55,
"NOTE_AS1": 58,
"NOTE_B1": 62,
"NOTE_C2": 65,
"NOTE_CS2": 69,
"NOTE_D2": 73,
"NOTE_DS2": 78,
"NOTE_E2": 82,
"NOTE_F2": 87,
"NOTE_FS2": 93,
"NOTE_G2": 98,
"NOTE_GS2": 104,
"NOTE_A2": 110,
"NOTE_AS2": 117,
"NOTE_B2": 123,
"NOTE_C3": 131,
"NOTE_CS3": 139,
"NOTE_D3": 147,
"NOTE_DS3": 156,
"NOTE_E3": 165,
"NOTE_F3": 175,
"NOTE_FS3": 185,
"NOTE_G3": 196,
"NOTE_GS3": 208,
"NOTE_A3": 220,
"NOTE_AS3": 233,
"NOTE_B3": 247,
"NOTE_C4": 262,
"NOTE_CS4": 277,
"NOTE_D4": 294,
"NOTE_DS4": 311,
"NOTE_E4": 330,
"NOTE_F4": 349,
"NOTE_FS4": 370,
"NOTE_G4": 392,
"NOTE_GS4": 415,
"NOTE_A4": 440,
"NOTE_AS4": 466,
"NOTE_B4": 494,
"NOTE_C5": 523,
"NOTE_CS5": 554,
"NOTE_D5": 587,
"NOTE_DS5": 622,
"NOTE_E5": 659,
"NOTE_F5": 698,
"NOTE_FS5": 740,
"NOTE_G5": 784,
"NOTE_GS5": 831,
"NOTE_A5": 880,
"NOTE_AS5": 932,
"NOTE_B5": 988,
"NOTE_C6": 1047,
"NOTE_CS6": 1109,
"NOTE_D6": 1175,
"NOTE_DS6": 1245,
"NOTE_E6": 1319,
"NOTE_F6": 1397,
"NOTE_FS6": 1480,
"NOTE_G6": 1568,
"NOTE_GS6": 1661,
"NOTE_A6": 1760,
"NOTE_AS6": 1865,
"NOTE_B6": 1976,
"NOTE_C7": 2093,
"NOTE_CS7": 2217,
"NOTE_D7": 2349,
"NOTE_DS7": 2489,
"NOTE_E7": 2637,
"NOTE_F7": 2794,
"NOTE_FS7": 2960,
"NOTE_G7": 3136,
"NOTE_GS7": 3322,
"NOTE_A7": 3520,
"NOTE_AS7": 3729,
"NOTE_B7": 3951,
"NOTE_C8": 4186,
"NOTE_CS8": 4435,
"NOTE_D8": 4699,
"NOTE_DS8": 4978
}
def SecondMelodie():
        global song
        try:
            
            mysong =['The Legend of Zelda theme', 88, 'NOTE_AS4', '-2', 'NOTE_F4', '8', 'NOTE_F4', '8', 'NOTE_AS4', '8', 'NOTE_GS4', '16', 'NOTE_FS4', '16', 'NOTE_GS4', '-2', 'NOTE_AS4', '-2', 'NOTE_FS4', '8', 'NOTE_FS4', '8', 'NOTE_AS4', '8', 'NOTE_A4', '16', 'NOTE_G4', '16', 'NOTE_A4', '-2', 'REST', '1', 'NOTE_AS4', '4', 'NOTE_F4', '-4', 'NOTE_AS4', '8', 'NOTE_AS4', '16', 'NOTE_C5', '16', 'NOTE_D5', '16', 'NOTE_DS5', '16', 'NOTE_F5', '2', 'NOTE_F5', '8', 'NOTE_F5', '8', 'NOTE_F5', '8', 'NOTE_FS5', '16', 'NOTE_GS5', '16', 'NOTE_AS5', '-2', 'NOTE_AS5', '8', 'NOTE_AS5', '8', 'NOTE_GS5', '8', 'NOTE_FS5', '16', 'NOTE_GS5', '-8', 'NOTE_FS5', '16', 'NOTE_F5', '2', 'NOTE_F5', '4', 'NOTE_DS5', '-8', 'NOTE_F5', '16', 'NOTE_FS5', '2', 'NOTE_F5', '8', 'NOTE_DS5', '8', 'NOTE_CS5', '-8', 'NOTE_DS5', '16', 'NOTE_F5', '2', 'NOTE_DS5', '8', 'NOTE_CS5', '8', 'NOTE_C5', '-8', 'NOTE_D5', '16', 'NOTE_E5', '2', 'NOTE_G5', '8', 'NOTE_F5', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '8', 'NOTE_F4', '16', 'NOTE_F4', '8', 'NOTE_AS4', '4', 'NOTE_F4', '-4', 'NOTE_AS4', '8', 'NOTE_AS4', '16', 'NOTE_C5', '16', 'NOTE_D5', '16', 'NOTE_DS5', '16', 'NOTE_F5', '2', 'NOTE_F5', '8', 'NOTE_F5', '8', 'NOTE_F5', '8', 'NOTE_FS5', '16', 'NOTE_GS5', '16', 'NOTE_AS5', '-2', 'NOTE_CS6', '4', 'NOTE_C6', '4', 'NOTE_A5', '2', 'NOTE_F5', '4', 'NOTE_FS5', '-2', 'NOTE_AS5', '4', 'NOTE_A5', '4', 'NOTE_F5', '2', 'NOTE_F5', '4', 'NOTE_FS5', '-2', 'NOTE_AS5', '4', 'NOTE_A5', '4', 'NOTE_F5', '2', 'NOTE_D5', '4', 'NOTE_DS5', '-2', 'NOTE_FS5', '4', 'NOTE_F5', '4', 'NOTE_CS5', '2', 'NOTE_AS4', '4', 'NOTE_C5', '-8', 'NOTE_D5', '16', 'NOTE_E5', '2', 'NOTE_G5', '8', 'NOTE_F5', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '16', 'NOTE_F4', '8', 'NOTE_F4', '16', 'NOTE_F4', '8']

            tempo = mysong[1] 
            for thisNote in range(2, len(mysong), 2):
                
                noteduration = duration(tempo, int(mysong[thisNote+1]))
                
                if (mysong[thisNote] == "REST"):
                    be_quiet()
                else:
                    playtone(notes[mysong[thisNote]])
                
                sleep(noteduration*0.9/1000) # we only play the note for 90% of the duration...
                be_quiet()
                sleep(noteduration*0.1/1000) # ... and leave 10% as a pause between notes
        except :
            return

            

while True:
    #print(vol)
    if song == True:
        print("premier music")
        PremierMelodie()
    else:
        print("deuxieme lecture")
        SecondMelodie()


