import asyncio
import websockets
import plotter

async def main():
  async with websockets.connect("ws://localhost:8765") as websocket:
    async def send(msg):
      await websocket.send(msg)

    p = plotter.Plotter(send)
    await p.rectTest()

asyncio.run(main())
