import json
import sys

from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        match self.path:
            case '/api/display':
                self.get_display()
            case '/api/setup':
                self.get_setup()
            case '/bitmap':
                self.get_bitmap()
            case _:
                self.not_found()

    def get_base_url(self):
        protocol = 'http'
        if self.headers.get('X-Forwarded-Proto'):
            protocol = self.headers['X-Forwarded-Proto']
        host = self.headers.get('Host', None)
        if host:
            return f'{protocol}://{host}'
        else:
            return f'/'

    def get_bitmap(self):
        self.send_response(200)
        self.send_header('Content-Type', 'image/bmp')
        self.end_headers()
        with content_file.open('rb') as f:
            self.wfile.write(f.read())

    def get_display(self):
        base_url = self.get_base_url()
        self.send_json_response(
            {
                'status': 0,
                'image_url': f'{base_url}/bitmap',
                'filename': 'content',
                'update_firmware': False,
                'firmware_url': None,
                'refresh_rate': '1800',
                'reset_firmware': False
            }
        )

    def get_setup(self):
        base_url = self.get_base_url()
        self.send_json_response(
            {
                'status': 200,
                'api_key': '123456789',
                'friendly_id': 'TRMNL-123',
                'image_url': f'{base_url}/bitmap',
                'filename': 'content',
            }
        )

    def not_found(self):
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Not Found')

    def send_json_response(self, json_body: dict[str, Any] | list[Any]):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(json_body).encode('utf-8'))


class Server(HTTPServer):
    def __init__(self, host: str, port: int, content_file: Path):
        super().__init__((host, port), Handler)
        self.content_file = content_file


print('Serving...')

content_dir = Path('../tmp')
content_dir.mkdir(parents=True, exist_ok=True)
content_file = content_dir / 'content.bmp'

server = None
try:
    server = Server('', 4000, content_file)
    server.serve_forever()
except KeyboardInterrupt:
    server and server.server_close()
except Exception as e:
    print(e)
    sys.exit(1)

sys.exit(0)
