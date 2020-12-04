from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

# This is just a simple blinking led

led = LED(14)
led.blink(2, 1)

pause()
