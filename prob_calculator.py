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
  success = 0
  
  #Experiments Loop
  for i in range(num_experiments):
    fake = copy.deepcopy(hat)
    
    #Drawing balls
    drawn_balls = fake.draw(num_balls_drawn)
    dballs = dict()
    for ball in drawn_balls:
      dballs[ball] = dballs.get(ball, 0) + 1

    #Checking of drawn_balls
    check = True
    for (k,v) in expected_balls.items():
      if k not in dballs.keys() or expected_balls[k] > dballs[k]:
        check = False
        break
      
    if check:
      success = success + 1

  return (success / num_experiments)