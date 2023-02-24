import datetime


class character:
  def __init__(self, name, isman, age):
    self.name = name
    self.isman = isman
    self.age = age

  def __str__(self):
    return f"{self.name}, witaj w naszej aplikacji!"

p1 = character("Mateusz", True, 19)

print(p1)

class MyClass:
  x=1

p1 = MyClass()

print(MyClass())

x = datetime.datetime.now()

print(x.strftime("%X"))

print(datetime.datetime.now())

import math

x = math.pi

print(x)