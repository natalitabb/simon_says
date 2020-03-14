from gpiozero import LED, Button
from time import sleep
from random import sample

led_red = LED(25)
led_yellow = LED(16)
led_green = LED(24)
led_blue = LED(23)

but_red = Button(17)
but_yellow = Button(27)
but_blue = Button(22)
but_green = Button(6)


def led_red_on():
  print "red"
  led_red.on()


def led_yellow_on():
  print "yellow"
  led_yellow.on()


def led_green_on():
  print "green"
  led_green.on()


def led_blue_on():
  print "blue"
  led_blue.on()


but_red.when_pressed = led_red_on
but_red.when_released = led_red.off

but_yellow.when_pressed = led_yellow_on
but_yellow.when_released = led_yellow.off

but_blue.when_pressed = led_blue_on
but_blue.when_released = led_blue.off

but_green.when_pressed = led_green_on
but_green.when_released = led_green.off

print "START!!!!"
sleep(1000000)
