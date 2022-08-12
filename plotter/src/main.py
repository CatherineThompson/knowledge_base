import config
import network

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
