from gpiozero import LED, Button
from time import sleep
from random import sample

led_red = LED(25)
led_yellow = LED(16)
led_green = LED(24)
led_blue = LED(23)


def blink(color, t):
  if color == 'red':
    led = led_red
  elif color == 'yellow':
    led = led_yellow
  elif color == 'green':
    led = led_green
  else:
    led = led_blue

  led.on()
  sleep(t)
  led.off()


blink('red', 1)
blink('yellow', 1)
blink('blue', 1)
blink('grenn', 1)

colors = ['red', 'yellow', 'green', 'blue']
n = 1
while n <= 5:
  rand_color = sample(colors, 1)
  print "round: ", n, "color: ", rand_color[0]
  blink(rand_color[0], 1)
  sleep(1)
  n = n + 1
