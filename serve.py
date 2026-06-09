import http.server, functools

DIR = "/Users/hani/Documents/הרצאה טורק"
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIR)
PORT = 8000

# ThreadingHTTPServer handles requests concurrently — a streaming video no longer
# blocks the single worker (which made the tab spin and other videos fail to load).
http.server.ThreadingHTTPServer.allow_reuse_address = True
http.server.ThreadingHTTPServer.daemon_threads = True
with http.server.ThreadingHTTPServer(("localhost", PORT), Handler) as httpd:
    print("serving", DIR, f"on http://localhost:{PORT}")
    httpd.serve_forever()
