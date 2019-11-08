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