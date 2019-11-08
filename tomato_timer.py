from microbit import *
import utime as time

def is_button_a_pressed():
    return button_a.is_pressed()

def is_button_b_press():
    return button_b.is_pressed()

def show_image(pixels):
    display.show(Image(pixels))

def time_now():
    return time.ticks_ms()

import math

def get_countdown_image(count):
	pixels = []
	for i in range(25):
		if i % 5 == 0 and i > 0:
			pixels.append(':')
		pixels.append('0' if i >= count else '5')
	pixels.reverse()
	return ''.join(pixels)

start = time_now()
in_break = False
while True:
    if is_button_a_pressed():
        start = time_now()
        in_break = not in_break
    if is_button_b_press():
        start = start - 60000

    minutes_target = 5 if in_break else 25

    count = minutes_target - math.floor((time_now() - start) / 60000)

    pixels = get_countdown_image(count) if count > 0 else ('55555:55555:55555:55555:55555' if strobe_on else '00000:00000:00000:00000:00000')
    show_image(pixels)
