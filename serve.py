import http.server, socketserver, functools

DIR = "/Users/hani/Documents/הרצאה טורק"
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIR)
socketserver.TCPServer.allow_reuse_address = True
PORT = 8000
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print("serving", DIR, f"on http://localhost:{PORT}")
    httpd.serve_forever()
