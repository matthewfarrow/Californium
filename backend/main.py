
import http.server
import socketserver

from web3 import Web3
import os

# ipcpath = os.path.join(os.path.expanduser('~'), '.local/share/trinity/ropsten/ipcs-eth1/jsonrpc.ipc')
# w3provider = Web3.IPCProvider(ipcpath)

projectId = 'eacb0a5460c944c7a0b3b0625e5259a1'
network = 'mainnet'
w3provider = Web3.HTTPProvider("https://"+network+".infura.io/v3/"+projectId)

w3 = Web3(w3provider)

PORT = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write('OOF'.encode())
        elif self.path == '/s':
            content_type = 'text/html'
            content = 'bullshit detected, reboot computer now'
            self.send_response(200)
            self.send_header("Content-type", content_type)
            self.end_headers()
            self.wfile.write(content.encode())
        else:
            self.send_error(404)

handler = MyHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
