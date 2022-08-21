from machine import Pin
import time

class Stepper:
  # UP = 0
  # DOWN = 1

  def __init__(self, stepPin, dirPin, delay, invertDir = False):
    self.stepPin = Pin(stepPin, Pin.OUT)
    self.stepPin(0)
    self.dirPin = Pin(dirPin, Pin.OUT)
    self.dirPin(0)
    self.delay = delay

    self.UP = 0
    self.DOWN = 1

    if invertDir:
      self.UP = 1
      self.DOWN = 0

  def step(self, dir):
    print('stepping')
    self.dirPin(dir)

    self.stepPin(1)
    time.sleep_ms(self.delay)
    self.stepPin(0)
    time.sleep_ms(self.delay)
