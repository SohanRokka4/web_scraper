from http.server import HTTPServer, BaseHTTPRequestHandler
class request_handeler(BaseHTTPRequestHandler):
    #...page template...

    def do_get(self):
        page = self.cerate_page()
        self.send_page(page)

    def create_page(self):
        # ...fill in...

    def send_page(self,page):
        # ...fill in...
