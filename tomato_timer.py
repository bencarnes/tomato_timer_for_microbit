from microbit import *
import utime as time

def get_button_a_presses():
    return button_a.get_presses()

def get_button_b_presses():
    return button_b.get_presses()

def show_image(pixels):
    display.show(Image(pixels))

def time_now():
    return time.ticks_ms()

import math

def was_button_a_pressed():
    # getting the number of pressses also resets the number or presses.
    return get_button_a_presses() > 0

def was_button_b_pressed():
    # getting the number of pressses also resets the number or presses.
    return get_button_b_presses() > 0

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
    if was_button_a_pressed():
        start = time_now()
        in_break = not in_break
    if was_button_b_pressed():
        start = start - 60000

    minutes_target = 5 if in_break else 25

    count = minutes_target - math.floor((time_now() - start) / 60000)

    strobe_on = math.floor((time_now() - start) / 1000) % 2

    pixels = get_countdown_image(count) if count > 0 else ('55555:55555:55555:55555:55555' if strobe_on else '00000:00000:00000:00000:00000')
    show_image(pixels)
