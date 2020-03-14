#!/usr/bin/env python

from random import sample
from gpiozero import LED, Button
from time import sleep

led_green = LED(23)
led_yellow = LED(24)
led_blue = LED(16)
led_red = LED(20)

but_red = Button(21)
but_yellow = Button(15)
but_blue = Button(7)
but_green = Button(14)

colors = ['red', 'yellow', 'green', 'blue']
higher_score = 0

score = 0
simon_colors = []
user_colors = []
c = 0
result = True


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


def blink_colors(color_list):
  # print "Simon colors: ", simon_colors
  for c in color_list:
    blink(c, 1)
    sleep(0.5)


def led_red_on():
  global ready
  if not ready:
    return

  global result
  led_red.on()
  result = check('red')


def led_yellow_on():
  global ready
  if not ready:
    return

  global result
  led_yellow.on()
  result = check('yellow')


def led_green_on():
  global ready
  if not ready:
    ready = True
    return

  global result
  led_green.on()
  result = check('green')


def led_blue_on():
  global ready
  if not ready:
    return

  global result
  led_blue.on()
  result = check('blue')


def check(color):
  global c, user_colors, simon_colors
  # print c, " - Pressed: ", color
  user_colors.append(color)
  c = c + 1
  for i in range(0, c):
    if simon_colors[i] != user_colors[i]:
      return False
  return True


def wait_for_user_colors():
  global c, score, user_colors
  # print "Users turn, press the colors..."
  while (c < score) and (result == True):
    sleep(1)
    # print "User times pressed: ", c, ". Score: ", score, ". Result: ", result
  # print "User colors: ", user_colors
  # print "Simon colors: ", simon_colors
  sleep(1)


def turn_all_leds_on(n, t):
  i = 1
  while i <= n:
    led_red.on()
    led_yellow.on()
    led_green.on()
    led_blue.on()
    sleep(t)
    led_red.off()
    led_yellow.off()
    led_green.off()
    led_blue.off()
    sleep(t)
    i = i + 1


but_red.when_pressed = led_red_on
but_red.when_released = led_red.off
but_yellow.when_pressed = led_yellow_on
but_yellow.when_released = led_yellow.off
but_blue.when_pressed = led_blue_on
but_blue.when_released = led_blue.off
but_green.when_pressed = led_green_on
but_green.when_released = led_green.off


blink('green', 1)
blink('yellow', 1)
blink('blue', 1)
blink('red', 1)

ready = False
while True:
  print "Press green button to start!!"
  while not ready:
    sleep(0.5)
  turn_all_leds_on(1, 0.5)

  while result:
    score = score + 1
    user_colors = []
    c = 0
    print "Round: ", score, "| Score: ", score - 1, "| Higher Score: ", higher_score

    rand_color = sample(colors, 1)
    simon_colors.append(rand_color[0])
    blink_colors(simon_colors)
    wait_for_user_colors()
    # print "--------------------------------------------------------"

  ready = False
  score = score - 1
  turn_all_leds_on(3, 1)

  print "User colors: ", user_colors
  print "Simon colors: ", simon_colors
  print "--------------------------------------------------------"

  if score > higher_score:
    print "You beat the higher score of", higher_score, "!!!"
    higher_score = score

  print "Score: ", score
  print "Higher Score: ", higher_score
  print "========================================================"
  print

  score = 0
  simon_colors = []
  result = True
