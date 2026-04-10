#!/usr/bin/env python3
import http.server, socketserver, os

PORT = 3000
ROOT = '/Users/rajivsurya/Documents/email-editor'

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0]
        if path == '/':
            path = '/index.html'
        file_path = ROOT + path
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                data = f.read()
            ext = os.path.splitext(file_path)[1]
            ct = {'html': 'text/html', 'css': 'text/css', 'js': 'application/javascript',
                  'png': 'image/png', 'jpg': 'image/jpeg', 'svg': 'image/svg+xml'}.get(ext.lstrip('.'), 'application/octet-stream')
            self.send_response(200)
            self.send_header('Content-Type', ct + '; charset=utf-8')
            self.send_header('Content-Length', len(data))
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_response(404)
            self.end_headers()
    def log_message(self, fmt, *args):
        pass

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    httpd.serve_forever()
