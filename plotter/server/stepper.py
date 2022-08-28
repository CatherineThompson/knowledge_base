from machine import Pin
import uasyncio as asyncio
import utime

class Stepper:
  def __init__(self, stepPin, dirPin, delay, invertDir = False):
    self.stepPin = Pin(stepPin, Pin.OUT)
    self.stepPin(0)
    self.dirPin = Pin(dirPin, Pin.OUT)
    self.dirPin(0)
    self.dir = 0
    self.delay = delay

    self.UP = 0
    self.DOWN = 1

    if invertDir:
      self.UP = 1
      self.DOWN = 0

  def step(self, dir):
    if dir != self.dir:
      self.dirPin(dir)
      self.dir = dir

    self.stepPin(1)
    utime.sleep_ms(self.delay)
    self.stepPin(0)
    utime.sleep_ms(self.delay)
