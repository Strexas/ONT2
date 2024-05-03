"""Inteface for creating custom nodes"""
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import pickle
import multiprocessing


class NodeInterface(HTTPServer):
    class RequestHandler(BaseHTTPRequestHandler):
        def __init__(self, request, client_address, server):
            super().__init__(request, client_address, server)
            self.waiting_to_give = False

        def protocol(self, func):
            pass

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            data_bytes = self.rfile.read(content_length)

            data = pickle.loads(data_bytes)

            self.send_response(200)
            self.send_header("Content-type", "application/octet-stream")
            self.end_headers()

            self.wfile.write(pickle.dumps(data))

    def __init__(self, server_address):
        super().__init__(server_address, self.RequestHandler)




def start_server(node, ip, port):
    webServer = HTTPServer((ip, port), node)

    print(node, "Started: ", ip, port)
    start = time.time()
    try:
        webServer.serve_forever()
    except KeyboardInterrupt as e:
        webServer.server_close()
    print("Server stopped. It worked: ", time.time() - start)

def start_node(node, ip, port):
    process = multiprocessing.Process(target=start_server, args=(node, ip, port))
    process.start()


start_node(NodeInterface, "localhost", 8081)
start_node(NodeInterface, "localhost", 8082)
start_node(NodeInterface, "localhost", 8083)
start_node(NodeInterface, "localhost", 8084)
start_node(NodeInterface, "localhost", 8085)
start_node(NodeInterface, "localhost", 8086)
start_node(NodeInterface, "localhost", 8087)
start_node(NodeInterface, "localhost", 8088)
start_node(NodeInterface, "localhost", 8089)
start_node(NodeInterface, "localhost", 8090)
