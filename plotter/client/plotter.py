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
  
  async def move(self, x, y):
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

    print(leftSteps)
    print(rightSteps)

    ratio = leftSteps/rightSteps
    while leftSteps + rightSteps > 0:
        r = leftSteps/rightSteps
        if r >= ratio:
          await self.send('L %s' % leftDir)
          leftSteps -= 1
        else:
          await self.send('R %s' % rightDir)
          rightSteps -= 1

    # TODO: change to actual position (floor)
    self.x = x
    self.y = y

  async def rectTest(self):
      await self.move(25, 25)
      await self.move(75, 25)
      await self.move(75, 75)
      await self.move(25, 75)
      await self.move(25, 25)
      await self.move(50, 50)
