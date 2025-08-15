from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Write message
        message = """
        <html>
            <head><title>Welcome</title></head>
            <body style="font-family: Arial; text-align: center; margin-top: 50px;">
                <h1>Hello from Docker Python App! 🚀</h1>
                <p>This is served without Flask.</p>
            </body>
        </html>
        """
        self.wfile.write(message.encode('utf-8'))

# Run server
def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on port 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

