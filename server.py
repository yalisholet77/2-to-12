from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        # Setting the content type
        if self.path.endswith(".html"):
            content_type = 'text/html'
        elif self.path.endswith(".css"):
            content_type = 'text/css'
        elif self.path.endswith(".js"):
            content_type = 'application/javascript'
        else:
            content_type = 'text/plain'

        try:
            # Reading the file content
            with open(self.path[1:], 'rb') as file:  # Open in binary mode for universal compatibility
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "File not found")

# Specify the port
port = 8000
httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)

print(f"Serving at port {port}")
httpd.serve_forever()
