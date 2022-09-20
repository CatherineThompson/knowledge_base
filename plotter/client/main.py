import plotter
import config
import socket

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((config.SERVER_HOST, config.SERVER_PORT))

    def send(msg):
      s.send(msg.encode())

    p = plotter.Plotter(send)
    p.starTest()

  print('done')

main()
