# Add your Python code here. E.g.
from microbit import *
import utime as time
import math

def get_countdown_image(count):
	leds = []
	for i in range(25):
		if i % 5 == 0 and i > 0:
			leds.append(':')
		leds.append('0' if i >= count else '5')
	leds.reverse()
	return ''.join(leds)

start = time.ticks_ms()
while True:
    if button_a.is_pressed():
        start = time.ticks_ms()
    if button_b.is_pressed():
        start = start - 60000
    count = 25 - math.floor((time.ticks_ms() - start) / 60000)
    if count > 0:
        leds = get_countdown_image(count)
        img = Image(leds)
        display.show(img)
    else:
        strobe_on = math.floor((time.ticks_ms() - start) / 1000) % 2
        display.show(Image('55555:55555:55555:55555:55555') if strobe_on else Image('00000:00000:00000:00000:00000'))

