from machine import Pin, PWM

class Stepper:
  UP = 0
  DOWN = 1

  def __init__(self, step_pin, dir_pin, enable_pin, step_size):
    self.pwm = PWM(Pin(step_pin))
    self.dir_pin = Pin(dir_pin)
    self.step_size = step_size

  def move(self, dir, freq):
    self.dir_pin(dir)    
    self.pwm.duty_u16(32768)
    self.pwm.freq(int((freq / self.step_size))

  def stop(self):
    self.pwm.deinit()
