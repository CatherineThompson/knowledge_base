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
    self.max_freq = int(config.MAX_FREQ / config.STEP_SIZE)
  
  def move(self, x, y):
    c1_prev = calc.pyth(self.x, self.y, None)
    c1 = calc.pyth(x, y, None)
    left_dir = 1 if c1_prev - c1 > 0 else -1
    left_steps = math.floor(abs(c1_prev - c1) * self.projectionRatio / self.stepDistance)

    c2_prev = calc.pyth(100 - self.x, self.y, None)
    c2 = calc.pyth(100 - x, y, None)
    right_dir = 1 if c2_prev - c2 > 0 else -1
    right_steps = math.floor(abs(c2_prev - c2) * self.projectionRatio / self.stepDistance)

    print(x, y)
    print(left_steps, right_steps)

    d = left_steps if left_steps > right_steps else right_steps
    t = int(d / self.max_freq * 1000)
    left_freq = int(left_steps / d * self.max_freq) * left_dir
    right_freq = int(right_steps / d * self.max_freq) * right_dir

    self.send(f'{left_freq},{right_freq},{t}|')

    self.x = x
    self.y = y

  def rectTest(self):
    self.move(25, 25)
    self.move(75, 25)
    self.move(75, 75)
    self.move(25, 75)
    self.move(25, 25)
    self.move(50, 50)
