from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond with "I'm alive"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"I'm alive")  # Write bytes as the response body

# Define the server details
host = "localhost"
port = 8080

# Start the HTTP server
server = HTTPServer((host, port), SimpleHandler)
print(f"Server running at http://{host}:{port}/")
try:
    server.serve_forever()  # Keep the server running
except KeyboardInterrupt:
    print("\nShutting down the server.")
    server.server_close()
