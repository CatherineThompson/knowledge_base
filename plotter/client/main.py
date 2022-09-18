import plotter
import config
import socket

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((config.SERVER_HOST, config.SERVER_PORT))

    def send(msg):
      s.send(msg.encode())

    s.send("-1000,-1000".encode("utf-8"))
    # p = plotter.Plotter(send)
    # p.rectTest()

  print('done')

main()
