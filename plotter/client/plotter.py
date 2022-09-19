import config
import math
import calc
import time


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
    c1_prev = calc.pyth(self.x, self.y, None)
    c1 = calc.pyth(x, y, None)
    left_dir = 1 if c1_prev - c1 > 0 else -1
    left_steps = left_dir * math.floor(abs(c1_prev - c1) * self.projectionRatio / self.stepDistance)

    c2_prev = calc.pyth(100 - self.x, self.y, None)
    c2 = calc.pyth(100 - x, y, None)
    right_dir = 1 if c2_prev - c2 > 0 else -1
    right_steps = right_dir * math.floor(abs(c2_prev - c2) * self.projectionRatio / self.stepDistance)

    msg = f'{left_steps},{right_steps}|'
    print(msg)

    self.send(msg)

    self.x = x
    self.y = y

  def rectTest(self):
    self.move(30, 30)
    self.move(70, 30)
    self.move(70, 70)
    self.move(30, 70)
    self.move(30, 30)
    self.move(50, 50)
