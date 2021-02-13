
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

frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend/startbootstrap-simple-sidebar-gh-pages')

def filenameToMimeType(filename):
    if not '.' in filename:
        return 'application/octet-stream'

    ext = filename.split('.')[-1]

    types = {
        'css': 'text/css',
        'htm': 'text/html',
        'html': 'text/html',
        'jpeg': 'image/jpeg',
        'jpg': 'image/jpeg',
        'js': 'text/javascript',
        'json': 'application/json',
        'png': 'image/png',
        'txt': 'text/plain',
        'pdf': 'application/pdf',
        'xhtml': 'application/xhtml+xml',
        'gif': 'image/gif',
    }

    if not ext in types.keys():
        return 'application/octet-stream'

    return types[ext]

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""

        path = os.path.join(frontend_dir, self.path[1:])
        if os.path.isfile(path):
            self.send_response(200)
            print(path, filenameToMimeType(os.path.basename(path)))
            self.send_header("Content-type", filenameToMimeType(os.path.basename(path)))
            self.end_headers()
            with open(path, 'rb') as f:
                self.wfile.write(f.read())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(os.path.join(frontend_dir, '404.html'), 'rb') as f:
                self.wfile.write(f.read())

handler = MyHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    try:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
