import binascii
import hashlib
import websocket
try:
    import usocket as socket
except ImportError:
    import socket


def getAcceptKey(req):
    request = req.decode() 
    print('Content = %s' % request)
    magicString = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    lines = request.split('\r\n')
    for l in lines:
        if l.startswith('Sec-WebSocket-Key'):
            _, wskey = l.split(": ")
            print(wskey)
            c = wskey + magicString
            acceptkey = c.encode()
            h = hashlib.sha1(acceptkey)
            return binascii.b2a_base64(h.digest()).decode().replace("\n", "")


def StartServer(cmdCallback):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        req = conn.recv(1024)
        acceptKey = getAcceptKey(req)

        conn.send('HTTP/1.1 101 Switching Protocols\r\n')
        conn.send('Upgrade: websocket\r\n')
        conn.send('Connection: Upgrade\r\n')
        conn.send('Sec-WebSocket-Accept: %s\r\n' % acceptKey)
        conn.send('\r\n')

        ws = websocket.websocket(conn, True)
        while True:
            msg = ws.read(3)
            msgStr = msg.decode()

            if msgStr == 'end':
                break

            cmdCallback(msgStr)

        print("closing conn")
        conn.close()
