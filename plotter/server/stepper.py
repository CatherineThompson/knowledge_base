from machine import Pin, PWM

class Stepper:
  UP = 0
  DOWN = 1

  def __init__(self, step_pin, dir_pin, enable_pin, max_freq, step_size):
    self.pwm = PWM(Pin(step_pin))
    self.max_freq = max_freq
    self.step_size = step_size

  def move(self):
    self.pwm.duty_u16(32768)
    self.pwm.freq(int(self.max_freq / self.step_size))

  def stop(self):
    self.pwm.deinit()
