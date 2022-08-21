import config
import network
import ws
import stepper 

# connect to wifi access point
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
print(sta.ifconfig())

# setup plotter
leftStepper = stepper.Stepper(config.LEFT_STEP_PIN, config.LEFT_DIR_PIN, config.STEP_DELAY_MS, True)
rightStepper = stepper.Stepper(config.RIGHT_STEP_PIN, config.RIGHT_DIR_PIN, config.STEP_DELAY_MS)

def commands(cmd):
    print(cmd)
    motor, dir = cmd.split(' ')
    m = leftStepper if motor == 'L' else rightStepper
    d = m.UP if dir == 'U' else m.DOWN
    print('d: %s' % d)
    m.step(d)

ws.StartServer(commands)
