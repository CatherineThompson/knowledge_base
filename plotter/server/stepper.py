from machine import Pin
import rp2

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def move():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    wrap()

class Stepper:
  UP = 0
  DOWN = 1
  MAX_FREQ = 100000

  def __init__(self, stepPin, dirPin, enablePin, stateMachineId):
    self.stepPin = Pin(stepPin, Pin.OUT)
    self.stepPin(0)
    self.dirPin = Pin(dirPin, Pin.OUT)
    self.dirPin(0)
    self.enablePin = Pin(enablePin, Pin.OUT)
    self.enablePin(1)
    self.stateMachineId = stateMachineId

  def move(self, speed, dir):
    self.enablePin(0)
    self.dirPin(dir)
    self.motor = rp2.StateMachine(self.stateMachineId, move, freq=speed, set_base=self.stepPin)
    self.motor.active(1)

  def stop(self):
    self.motor.active(0)
    self.enablePin(1)
