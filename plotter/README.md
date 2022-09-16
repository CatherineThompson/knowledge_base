# Vertical Pen Plotter
Micropython implementation for a vertical pen plotter using a microcontroller such as a Raspberry Pi Pico W

## Setup

### Config
Create a `config.py` file in the `client` and `server` directories. 

<code>client/config.py</code>
```py
# in cm
SPOOL_DIAMETER = 10
BOARD_WIDTH = 100

# in degrees
STEP_SIZE = 1.8

# in Hz - cycles/steps per second
MAX_FREQ = 500

# 1 | 1/2 | 1/4 | 1/8 | 1/16
STEP_SIZE = 1/16

SERVER_HOST = "PYBD.localdomain"
SERVER_PORT = 8080
```

<code>server/config.py</code>
```py
WIFI_NAME = ''
WIFI_PASSWORD = ''

RIGHT_ENABLE_PIN = 16
RIGHT_STEP_PIN = 17
RIGHT_DIR_PIN = 18

LEFT_ENABLE_PIN = 19
LEFT_STEP_PIN = 20
LEFT_DIR_PIN = 21
```

### IDE Setup
It's helpful to configure your IDE to sync the `src` files to the microcontroller on save. Here is how to set this up on VSCode. 

1) Install `Run on Save` extension.
2) Add configuration to workspace `.vscode/settings.json`.

```json
{
  "emeraldwalk.runonsave": {
      "commands": [
          {
              "match": "plotter\\/server.*\\.py$",
              "cmd": "rshell rsync -m ~/src/knowledge_base/plotter/server /pyboard"
          },
      ],
  }
}
``` 

## Resources
https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/basics.html
https://github.com/dhylands/rshell
https://www.instructables.com/BLACKBOARD-V-PLOTTER/
https://stackoverflow.com/questions/35977916/generate-sec-websocket-accept-from-sec-websocket-key
https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_servers

### PIO State Machines
https://forums.raspberrypi.com/viewtopic.php?t=319959
https://vanhunteradams.com/Pico/Steppers/Lorenz.html

### GCode
https://ncviewer.com/
https://inkscape.org/~arpruss/%E2%98%85gcodeplot
https://github.com/PadLex/SvgToGcode

https://docs.python.org/3/howto/sockets.html
https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md#76-socket-programming
https://github.com/peterhinch/micropython-async/blob/master/v3/as_drivers/client_server/userver.py

# Stepper Motor
https://www.ti.com/lit/an/slyt482/slyt482.pdf?ts=1662772228247&ref_url=https%253A%252F%252Fwww.google.com%252F#:~:text=To%20accelerate%20a%20stepper%20from,tation%20uses%20only%20two%20timers.
