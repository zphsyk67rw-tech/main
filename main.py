#!/usr/bin/env python3

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at porteis", PORT)
    httpd.serve_forever()
