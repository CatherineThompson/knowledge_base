# Vertical Pen Plotter
Micropython implementation for a vertical pen plotter using a microcontroller such as a Raspberry Pi Pico W

## Setup

### Config
Create a `config.py` file in the `src` directory.

```py
WIFI_NAME = ''
WIFI_PASSWORD = ''

# in cm
SPOOL_DIAMETER = 10
BOARD_WIDTH = 100

# in degrees
STEP_SIZE = 1.8
STEP_DELAY_MS = 5

LEFT_STEP_PIN = 16
LEFT_DIR_PIN = 14 

RIGHT_STEP_PIN = 12
RIGHT_DIR_PIN = 13
```

### IDE Setup
It's helpful to configure your IDE to sync the `src` files to the microcontroller on save. Here is how to set this up on VSCode. 

1) Install `Run on Save` extension.
2) Add configuration to workspace `.vscode/settings.json`.

```json
"emeraldwalk.runonsave": {
    "commands": [
        {
            "match": "plotter\\/src.*\\.py$",
            "cmd": "rshell rsync -m ~/src/knowledge_base/plotter/src /pyboard"
        },
    ],
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

https://websockets.readthedocs.io/en/stable/reference/client.html

### GCode
https://ncviewer.com/
https://inkscape.org/~arpruss/%E2%98%85gcodeplot
https://github.com/PadLex/SvgToGcode