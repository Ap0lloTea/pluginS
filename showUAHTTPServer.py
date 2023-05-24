from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        user_agent = self.headers.get('User-Agent')
        print(f"User-Agent: {user_agent}")
        super().do_GET()

def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server(80)


