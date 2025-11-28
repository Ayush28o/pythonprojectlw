import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as http:
    print(f"Server is running on {PORT}")
    http.serve_forever()
    

   