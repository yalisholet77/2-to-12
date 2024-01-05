import http.server
import socketserver
import webbrowser
import threading

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Function to open the browser
def open_browser():
    webbrowser.open(f'http://localhost:{PORT}')

# Set up the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # Open the browser
    threading.Thread(target=open_browser).start()
    # Start the server
    httpd.serve_forever()
