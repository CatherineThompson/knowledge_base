# Marlin Polargraph

https://github.com/CatherineThompson/Marlin/tree/ct-polargraph

## Resources
https://reprap.org/wiki/RAMPS_1.4
https://marlinfw.org/docs/configuration/configuration.html#configuration.h
https://marlinfw.org/docs/gcode/G000-G001.html
https://www.marginallyclever.com/2021/10/friday-facts-4-how-to-marlin-polargraph/


## Bug
Can disable software endstops with `M211 S0` or change the code.
https://github.com/MarlinFirmware/Marlin/issues/23245

Relevant files: motion.cpp, polargraph.cpp, planner.cpp
Shared code with delta, scara, polargraph print types

## Helpful Gcode Commands
```
M114 - report current position
M502 - factory reset - initialize eeprom
M503 - report eeprom settings
G28 XY - home

M500
M501
```

## Debugging

Use SERIAL_POS, SERIAL_ECHO_MSG, serial docs

gcode-sender

## Fried Arduino Issues

1. Short circuited the board by connecting the endstop voltage to the ground. Seems to have damaged the voltage regulator on the mega. There is a visible bubble on the 3 pronged regulator. The board turns on and works fine when powered over usb, but stops communicating over usb when 12V power supply is turned on.

Likely fried the 5V regulator, which means the board cannot be powered over vin - https://forum.arduino.cc/t/ramps-1-4-arduino-mega/346489
https://docs.arduino.cc/learn/electronics/power-pins

2. Moved the mega ramps and reconnected the wires. The wired were connected correctly. Tried homing. The motors started to move, then stopped, smelled a burnt plastic. The power supply showed lower voltage, high amp and watt. The board does not communicate over usb. There is visible damage to the usb interface on the mega.

The Elegoo Mega 2560 has a recommended input voltage of 7-9V. Since the ramps 12V 5A powers the arduino, the supplied voltage was above range and likely fried the mega. 
https://reprap.org/wiki/RAMPS_24v
https://reprap.org/wiki/RAMPS_1.4#Power_Supply

TODO: Try removing the D1 diode and powering the mega over the usb. This is likely safer for the mega since providing power through the VIN pin does not have reverse polarity protection.
https://docs.arduino.cc/learn/electronics/power-pins#vin-pin-1

UPDATE: ^^ The above worked! Removing the D1 diode allows the mega to be powered with the 5V regulated usb connection.
