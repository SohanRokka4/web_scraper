from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):  # Fixed: inherit from BaseHTTPRequestHandler
    '''handle HTTP requests by returning a fixed 'page'.'''

    # Page to send back,
    Page = '''\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
'''

    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))  # Fixed: self.Page
        self.end_headers()
        self.wfile.write(self.Page.encode())  # Added .encode() for Python 3


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()