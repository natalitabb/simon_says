from random import randrange
import time
import getch

def random_color():
  color = randrange(4)
  return color

def show(color_list):
  for c in color_list:
    print(c),
    time.sleep(1)

  for _ in color_list:
    print("\b\b\b"),

def ask_color_list(total):
  input_list = []
  print("Enter color sequence: ")
  for _ in range(0,total):
    color = getch.getche()
    input_list.append(color)
  return input_list


color_list = []
equal_list = True
while equal_list:
  color = random_color()
  color_list.append(color)
  show(color_list)
  total = len(color_list)
  user_list = ask_color_list(total)
  equal_list = user_list == color_list
  
  if equal_list:
    print("Excellent!! Continue")
  else:
    print("Game Over")



