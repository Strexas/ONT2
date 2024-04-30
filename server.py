# Python 3 server example
import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer, CGIHTTPRequestHandler
import time
import pickle
import sys
import pandas as pd
import numpy as np

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        content_length = int(self.headers['Content-Length'])
        post_data_bytes = self.rfile.read(content_length)
        print(content_length)
        data = pickle.loads(post_data_bytes)
        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream")
        self.end_headers()

        self.wfile.write(pickle.dumps(f"data size: {sys.getsizeof(data) / 1024 / 1024}MB"))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data_bytes = self.rfile.read(content_length)

        data = pickle.loads(post_data_bytes)
        data[0] = data[0] + 1

        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream")
        self.end_headers()

        self.wfile.write(pickle.dumps(data))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
