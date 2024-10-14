import machine
class SERVO:
    def __init__(self,pin):
        self.pin =pin
        self.pwm = machine.PWM(self.pin)

    def turn(self, val):
        self.pwm.freq(100)
        self.pwm.duty_u16(int(val/180*13000+4000))
