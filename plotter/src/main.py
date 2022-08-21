import config
import network
import websocket
# import plotter

# connect to wifi access point
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
print(sta.ifconfig())

websocket.StartServer()

# setup plotter
# p = plotter.Plotter(leftStepper, rightStepper)

