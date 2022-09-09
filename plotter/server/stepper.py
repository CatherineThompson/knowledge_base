from machine import Pin, PWM

class Stepper:
  def __init__(self, step_pin, dir_pin, enable_pin):
    self.pwm = PWM(Pin(step_pin))
    self.dir_pin = Pin(dir_pin)
    # self.enable_pin = Pin(enable_pin)

  def move(self, dir, freq):
    self.dir_pin(dir)    
    # self.enable_pin.low()
    self.pwm.duty_u16(32768)
    self.pwm.freq(freq)

  def stop(self):
    self.pwm.deinit()
    # self.enable_pin.high()
