from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith('.gz'):
            self.send_header('Content-Encoding', 'gzip')
        super().end_headers()

httpd = HTTPServer(('localhost', 8000), CustomHandler)
httpd.serve_forever()
