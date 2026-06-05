import http.server, socketserver, functools

DIR = "/Users/hani/Documents/הרצאה טורק"
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIR)
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", 4599), Handler) as httpd:
    print("serving", DIR, "on http://127.0.0.1:4599")
    httpd.serve_forever()
