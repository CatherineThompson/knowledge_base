import config
import network
# import plotter

# connect to wifi access point
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
print(sta.ifconfig())

# setup plotter
# p = plotter.Plotter(leftStepper, rightStepper)

