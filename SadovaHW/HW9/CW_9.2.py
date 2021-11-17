import random

class Ghost(object):
  colors = ["red", "green", "blue", "yellow"]
  
  def __init__(self):
    self.color = random.choice(Ghost.colors)