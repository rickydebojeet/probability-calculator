import copy
import random
# Consider using the modules imported above.

class Hat:

  #Instansiation
  def __init__(self, **balls):
    self.contents = list()
    for (k, v) in balls.items:
      for x in v:
        self.contents.append(k)

  #Defining draw method
  def draw(self, num):
    tmp = copy.copy(self.contents)
    if num >= len(tmp):
      return tmp
    else:
      out = list()
      for x in num:
        out.append(tmp.pop(random.randrange(len(tmp))))
      return out



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
