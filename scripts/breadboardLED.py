from machine import Pin, PWM

pin = 4

PWM_pin = PWM(Pin(pin))

PWM_pin.freq(20)

percent = 50 

PWM_pin.duty_u16(percent*655)