from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        try:
            # Reading the file content
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

# Specify the port
port = 8000
httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)

print(f"Serving at port {port}")
httpd.serve_forever()
