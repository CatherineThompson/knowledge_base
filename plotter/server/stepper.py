from machine import Pin, PWM
import time
import math
import config

class Stepper:
  def __init__(self):
    self.step1 = Pin(config.LEFT_STEP_PIN, Pin.OUT)
    self.step2 = Pin(config.RIGHT_STEP_PIN, Pin.OUT)
    self.dir1 = Pin(config.LEFT_DIR_PIN, Pin.OUT)
    self.dir2 = Pin(config.RIGHT_DIR_PIN, Pin.OUT)
    max_freq = config.STEP_SIZE * 400
    min_freq = config.STEP_SIZE * 80
    self.max_delay = Stepper.speed_to_delay(max_freq)
    self.min_delay = Stepper.speed_to_delay(min_freq)
    # change in ramp up/ramp down delay per step
    self.delay_acc = 0.1
    self.steps_to_stop = int((self.min_delay - self.max_delay) / self.delay_acc)

    print("max_delay: ", self.max_delay)
    print("min_delay: ", self.min_delay)
    print("steps_to_stop: ", self.steps_to_stop)
    print()

  def speed_to_delay(freq):
    return int(500000 / freq)

  def move(self, steps, l_dir, l_rat, r_dir, r_rat):
    a_count = 0
    d_count = 0
    a_starting_delay = -1
    d_starting_delay = -1
    a_final_delay = -1
    d_final_delay = -1
    self.dir1.value(l_dir)
    self.dir2.value(r_dir)
    steps_to_stop = min(self.steps_to_stop, math.ceil(steps/2))
    print("real_steps_to_stop: ", steps_to_stop)

    l_step = 0
    r_step = 0
    for i in range(steps):
      steps_left = steps - i
      if steps_to_stop >= steps_left:
        delay = min(int(self.min_delay - steps_left * self.delay_acc), self.min_delay)
        if d_count == 0:
          d_starting_delay = delay
        d_count+=1
        d_final_delay = delay
      else:
        delay = max(int(self.min_delay - i * self.delay_acc), self.max_delay)
        if a_count == 0:
          a_starting_delay = delay
        a_count+=1
        a_final_delay = delay

      should_step_left = i == round(l_step * l_rat)
      should_step_right = i == round(r_step * r_rat)

      if should_step_left:
        self.step1.high()
      if should_step_right:
        self.step2.high()

      time.sleep_us(delay)

      if should_step_left:
        self.step1.low()
      if should_step_right:
        self.step2.low()

      time.sleep_us(delay)

      if should_step_left:
        l_step += 1
      if should_step_right:
        r_step += 1

    time.sleep_ms(500)
    
    print("acc_count: ", a_count)
    print("acc_start_delay: ", a_starting_delay)
    print("acc_final_delay", a_final_delay)
    print()

    print("dec_count: ", d_count)
    print("dec_start_delay", d_starting_delay)
    print("dec_final_delay", d_final_delay)
    print()
    print()
