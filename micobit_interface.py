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
