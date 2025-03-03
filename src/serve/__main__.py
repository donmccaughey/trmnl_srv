import json
import sys

from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/display':
            self.get_display()
        elif self.path == '/api/setup':
            self.get_setup()
        elif self.path == '/bitmap':
            self.get_bitmap()
        else:
            self.not_found()

    def get_bitmap(self):
        self.send_response(200)
        self.send_header('Content-Type', 'image/bmp')
        self.end_headers()
        with content_file.open('rb') as f:
            self.wfile.write(f.read())

    def get_display(self):
        self.send_json_response(
            {
                'status': 0,
                'image_url': 'https://localhost:4000/bitmap',
                'filename': 'content',
                'update_firmware': False,
                'firmware_url': None,
                'refresh_rate': '1800',
                'reset_firmware': False
            }
        )

    def get_setup(self):
        self.send_json_response(
            {
                'status': 200,
                'api_key': '123456789',
                'friendly_id': 'TRMNL-123',
                'image_url': 'https://localhost:4000/bitmap',
                'filename': 'content',
            }
        )

    def not_found(self):
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Not Found')

    def send_json_response(self, body):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body).encode('utf-8'))


class Server(HTTPServer):
    def __init__(self, host, port, content_file):
        super().__init__((host, port), Handler)
        self.content_file = content_file


print('Serving...')

content_dir = Path('../tmp')
content_dir.mkdir(parents=True, exist_ok=True)
content_file = content_dir / 'content.bmp'

try:
    server = Server('localhost', 4000, content_file)
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()

sys.exit(0)

