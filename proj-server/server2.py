from http.server import HTTPServer, BaseHTTPRequestHandler
class request_handeler(BaseHTTPRequestHandler):
    #...page template...

    def do_get(self):
        page = self.cerate_page()
        self.send_page(page)

    def create_page(self):
        values = {
            'date_time'   : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path
        }
        page = self.Page.format(**values)
        return page

    def send_page(self,page):
        # ...fill in...
