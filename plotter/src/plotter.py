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
    time.sleep_ms(20)
    self.stepPin(0)
    time.sleep_ms(15)

class Plotter:
  def __init__(self, leftStepper, rightStepper):
    self.leftStepper = leftStepper
    self.rightStepper = rightStepper
    self.stepDistance = 0.157
    self.x = 31.75
    self.y = 31.75
    self.width = 63.5
  
  def move(self, x, y):
    c1_prev = calc.pyth(self.x, self.y, None)
    c1 = calc.pyth(x, y, None)
    leftDir = Stepper.Up if c1_prev - c1 > 0 else Stepper.Down
    leftSteps = abs(c1_prev - c1) / self.stepDistance 

    c2_prev = calc.pyth(self.width - self.x, self.y, None)
    c2 = calc.pyth(self.width - x, y, None)
    rightDir = Stepper.Up if c2_prev - c2 > 0 else Stepper.Down
    rightSteps = abs(c2_prev - c2) / self.stepDistance 

    ratio = leftSteps/rightSteps
    while leftSteps + rightSteps > 0:
        r = leftSteps/rightSteps
        if r >= ratio:
            self.leftStepper.step(leftDir)
            leftSteps -= 1
        else:
            self.rightStepper.step(rightDir)
            rightSteps -= 1

    # TODO: change to actually position (floor)
    self.x = x
    self.y = y

    # TODO use ratio to step both at same time
    #for i in range(math.floor(leftSteps)):
    #  self.leftStepper.step(leftDir)

    #for i in range(math.floor(rightSteps)):
    #  self.rightStepper.step(rightDir)

  def rectTest(self):
    # for i in range(3)
      self.move(25, 25)
      self.move(40, 25)
      self.move(40, 40)
      self.move(25, 40)
      self.move(25, 25)
      self.move(31.75, 31.75)
      # self.move(20, 20)
      # self.move(10, 20)
      # self.move(20, 15)

def get_plotter(l_pin_step, l_pin_dir, r_pin_step, r_pin_dir):
    leftStepper = Stepper(l_pin_step, l_pin_dir)
    rightStepper = Stepper(r_pin_step, r_pin_dir)
    return Plotter(leftStepper, rightStepper)

