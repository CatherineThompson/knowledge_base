import config
import math
import calc
from pygcode import Line

class Plotter:
  def __init__(self, send):
    self.send = send

    # on a 100 by 100 unit grid - convert to board size with projectionRatio
    self.projectionRatio = config.BOARD_WIDTH / 100
    self.x = 50
    self.y = 50

    # how much the length of the string increase/decreases per step
    self.stepDistance = config.SPOOL_DIAMETER * math.pi / 360 * 1.8 * config.STEP_SIZE # 0.157 for full step
  
  def move(self, x, y):
    c1_prev = calc.pyth(self.x, self.y, None)
    c1 = calc.pyth(x, y, None)
    left_dir = 1 if c1_prev - c1 > 0 else -1
    left_steps = math.floor(abs(c1_prev - c1) * self.projectionRatio / self.stepDistance)

    c2_prev = calc.pyth(100 - self.x, self.y, None)
    c2 = calc.pyth(100 - x, y, None)
    right_dir = 1 if c2_prev - c2 > 0 else -1
    right_steps = math.floor(abs(c2_prev - c2) * self.projectionRatio / self.stepDistance)

    print(left_steps, right_steps)

    steps = left_steps if left_steps > right_steps else right_steps
    left_rat = round(steps / left_steps, 6) * left_dir
    right_rat = round(steps / right_steps, 6) * right_dir

    msg = f'{steps},{left_rat},{right_rat}\n'
    print(msg)

    self.send(msg)

    self.x = x
    self.y = y

  def rectTest(self):
    self.move(40, 40)
    self.move(60, 40)
    self.move(60, 60)
    self.move(40, 60)
    self.move(40, 40)
    self.move(60, 60)

  def starTest(self):
    with open('../assets/star_100_by_100_small.gcode', 'r') as fh:
      for line_text in fh.readlines():
          line = Line(line_text)

          if line.block.words[0] == "G01":
            if len(line.block.words) > 2:
              x = line.block.words[2].value
              y = line.block.words[3].value
              print(line.block.words)
              print(x, y)
              self.move(x, y)
