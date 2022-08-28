import config
import math
import calc

class Plotter:
  def __init__(self, send):
    self.send = send

    # on a 100 by 100 unit grid - convert to board size with projectionRatio
    self.projectionRatio = config.BOARD_WIDTH / 100
    self.x = 50
    self.y = 50

    # how much the length of the string increase/decreases per step
    self.stepDistance = config.SPOOL_DIAMETER * math.pi / 360 * config.STEP_SIZE # 0.157
  
  def move(self, x, y):
    if x > 100 or x < 0 or y > 100 or y < 0:
      return

    c1_prev = calc.pyth(self.x, self.y, None)
    c1 = calc.pyth(x, y, None)
    leftDir = 'U' if c1_prev - c1 > 0 else 'D'
    leftSteps = math.floor(abs(c1_prev - c1) * self.projectionRatio / self.stepDistance)

    c2_prev = calc.pyth(100 - self.x, self.y, None)
    c2 = calc.pyth(100 - x, y, None)
    rightDir = 'U' if c2_prev - c2 > 0 else 'D'
    rightSteps = math.floor(abs(c2_prev - c2) * self.projectionRatio / self.stepDistance)

    ratio = leftSteps/rightSteps if rightSteps else -1
    while leftSteps + rightSteps > 0:
      motor = 'L'

      if leftSteps == 0 or rightSteps == 0:
        motor = 'L' if rightSteps == 0 else 'R'
      else:
        r = leftSteps/rightSteps
        motor = 'L' if r > ratio else 'R'

      dir = rightDir if motor == 'R' else leftDir
      cmd = motor + dir
      self.send(cmd)
      
      if motor == 'L':
        leftSteps -= 1
      else:
        rightSteps -= 1


    # TODO: change to actual position (floor)
    self.x = x
    self.y = y

  def rectTest(self):
    self.move(25, 25)
    self.move(75, 25)
    self.move(75, 75)
    self.move(25, 75)
    self.move(25, 25)
    self.move(50, 50)
