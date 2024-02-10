from machine import Pin, PWM
import utime

color1 = PWM(Pin(14))
color1.freq(500)#HZ

color2 = PWM(Pin(15))
color2.freq(500)

color3 = PWM(Pin(12))
color3.freq(500)

for i in range(100):
    color1.duty_u16(i*655)
    color2.duty_u16((100-i)*655)
    color3.duty_u16(i*655)
    utime.sleep_ms(100)