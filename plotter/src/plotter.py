from machine import Pin
import time
import calc
import math

class Stepper:
  Up = 1
  Down = 0

  def __init__(self, stepPin, dirPin):
    self.stepPin = Pin(stepPin, Pin.OUT)
    self.stepPin(0)
    self.dirPin = Pin(dirPin, Pin.OUT)
    self.dirPin(0)

  def step(self, dir):
    self.dirPin(dir)

    self.stepPin(1)
    time.sleep_ms(100)
    self.stepPin(0)
    time.sleep_ms(100)

class Plotter:
  def __init__(self, leftStepper, rightStepper):
    self.leftStepper = leftStepper
    self.rightStepper = rightStepper
    self.stepDistance = 0.157
    self.x = 15
    self.y = 15
    self.width = 30
  
  def move(self, x, y):
    c1_prev = calc.pyth(self.x, self.y, None)
    c1 = calc.pyth(x, y, None)
    leftDir = Stepper.Up if c1_prev - c1 > 0 else Stepper.Down
    leftSteps = abs(c1_prev - c1) / self.stepDistance 

    c2_prev = calc.pyth(self.width - self.x, self.y, None)
    c2 = calc.pyth(self.width - x, y, None)
    rightDir = Stepper.Up if c2_prev - c2 > 0 else Stepper.Down
    rightSteps = abs(c2_prev - c2) / self.stepDistance 

    # TODO: change to actually position (floor)
    self.x = x
    self.y = y

    # TODO use ratio to step both at same time
    for i in range(math.floor(leftSteps)):
      self.leftStepper.step(leftDir)

    for i in range(math.floor(rightSteps)):
      self.rightStepper.step(rightDir)

  def rectTest(self):
    # for i in range(3)
      self.move(10, 15)
      self.move(10, 20)
      self.move(20, 20)
      self.move(20, 15)
      self.move(10, 15)
      # self.move(20, 20)
      # self.move(10, 20)
      # self.move(20, 15)
