import uasyncio as asyncio


def decode_message(data):
    msg = data.decode()
    m = msg.split('|')
    return m

class Server:

    def __init__(self, q, host='0.0.0.0', port=8080, backlog=1, timeout=20):
        self.q = q
        self.host = host
        self.port = port
        self.backlog = backlog
        self.timeout = timeout

    async def run(self):
        print('Awaiting client connection.')
        self.cid = 0
        self.server = await asyncio.start_server(self.run_client, self.host, self.port, self.backlog)
        while True:
            await asyncio.sleep(100)

    async def run_client(self, sreader, swriter):
        self.cid += 1
        print('Got connection from client', self.cid)
        try:
            while True:
                try:
                    data = await asyncio.wait_for(sreader.readline(), self.timeout)
                except asyncio.TimeoutError:
                    data = b''
                if data == b'':
                    raise OSError
                msg = decode_message(data)
                for cmd in msg:
                    if cmd != '':
                        self.q.put_nowait(cmd)
        except OSError:
            pass
        print('Client {} disconnect.'.format(self.cid))
        await sreader.wait_closed()
        print('Client {} socket closed.'.format(self.cid))

    async def close(self):
        print('Closing server')
        self.server.close()
        await self.server.wait_closed()
        print('Server closed.')
