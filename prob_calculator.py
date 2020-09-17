import copy
import random
# Consider using the modules imported above.

class Hat:

  #Instansiation
  def __init__(self, **balls):
    self.contents = list()
    for (k, v) in balls.items():
      for x in range(v):
        self.contents.append(k)

  #Defining draw method
  def draw(self, num):
    if num >= len(self.contents):
      return self.contents
    else:
      out = list()
      for x in range(num):
        out.append(self.contents.pop(random.randrange(len(self.contents))))
      return out



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
