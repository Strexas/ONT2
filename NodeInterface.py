"""Inteface for creating custom nodes"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import pickle
import sys


class NodeInterface(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data_bytes = self.rfile.read(content_length)

        data = pickle.loads(data_bytes)

        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream")
        self.end_headers()

        self.wfile.write(pickle.dumps(data))


if __name__ == "__main__":
    webServer = HTTPServer(("localhost", 8080), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
