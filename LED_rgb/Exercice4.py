from machine import Pin
Button = Pin(16,Pin.IN)
miniFan = Pin(18,Pin.OUT)

while True:
    val= Button.value()
    if val==1:
        miniFan.value(1)
    else:
        miniFan.value(0)