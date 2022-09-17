import config
import time
from stepper import Stepper
from machine import PWM, Pin, Timer
import uasyncio as asyncio
import rp2

def pwm_demo():
    pwm = PWM(Pin(config.LEFT_STEP_PIN))
    pwm.duty_u16(32768)
    pwm.freq(8000)

    time.sleep(5)

    pwm.deinit()

def accel_pwm_demo():
    pwm = PWM(Pin(config.LEFT_STEP_PIN))
    pwm.duty_u16(32768)
    for i in range(0):
        pwm.freq(i * 200 + 500)
        time.sleep_ms(10)

    time.sleep(5)

    for i in range(200):
        pwm.freq((200 - i) * 200 + 500)
        time.sleep_ms(10)

    pwm.deinit()

def accel_demo():
  stepper = Stepper()
  for i in range(20):
    stepper.move((i+1)*(i+1)*50, 1, 4)


@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def move():
  # pull off fifo and move from output shift register to y scratch register
  pull()
  mov(y, osr)

  # # pull off fifo and move from output shift register to x scratch register
  # pull()
  # mov(x, osr) # num steps

  # # jump to end label if x is 0
  # jmp(not_x, "end")

  # # wrap_target()
  # # set(pins, 1)   [2]
  # # nop()          [2]
  # # set(pins, 0)   [2]
  # # nop()          [2]
  # # wrap()

  # # label("loop")
  # # jmp(not_osre, "step") # skip moving y register contents back to osr if osr is not empty
  # # mov(osr, y)
  
  # label("step")
  wait(1, irq, 0)
  a = 31
  # mov(a, y)
  set(pins, y)   [a] # 
  # # nop()          [1] # arificial delay of about 2 cycles
  set(pins, y)   [a]
  # # nop()          [1]

  # jmp(x_dec,"step")

  # # out(pins, 4) [2] # takes bits from osr and puts them into pins
  # # nop() [2]

  # label("end")
  # irq(rel(0))
    
def pio_interupt(m):
  print("done")

def pio_demo():
  en = Pin(config.LEFT_ENABLE_PIN, Pin.OUT)
  en.low()

  motor = rp2.StateMachine(0, move, freq=100000, set_base=Pin(config.LEFT_STEP_PIN))
  # 8000 cycles per sec
  # 100000 instruction cycles per sec
  # 100000 = 8000(2 + 2x)


  motor.irq(pio_interupt)
  motor.active(1)

  time.sleep(2)

  motor.active(0)
    
count = 0
def timer_demo():
  def tick(t):
    global count
    if count%2500 == 0: 
      print('tick')

    count+=1
      

  tim = Timer()
  tim.init(freq=5000, mode=Timer.PERIODIC, callback=tick)

def delay_demo():
    pin = Pin(config.LEFT_STEP_PIN, Pin.OUT)
    for i in range(50000):
        pin.high()
        time.sleep_us(100)
        pin.low()
        time.sleep_us(100)

    time.sleep(2)
