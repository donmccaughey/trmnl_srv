import json
import sys

from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_request_details()
        match self.path:
            case '/api/display':
                self.get_display()
            case '/api/setup':
                self.get_setup()
            case '/bitmap':
                self.get_bitmap()
            case _:
                self.not_found()

    def do_POST(self):
        self.log_request_details()
        match self.path:
            case '/api/log':
                self.post_log()
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
        # self.send_header('Content-Type', 'image/bmp')
        self.send_header('Content-Type', 'image/png')
        self.end_headers()
        # with content_file.open('rb') as f:
        with content_file2.open('rb') as f:
            self.wfile.write(f.read())
        self.log_request(200)

    def get_display(self):
        base_url = self.get_base_url()
        self.send_json_response(
            {
                'filename': 'content.bmp',
                'firmware_url': None,
                'image_url': f'{base_url}/bitmap',
                'image_url_timeout': 0,
                'refresh_rate': '300',
                'reset_firmware': False,
                'special_function': 'none',
                'update_firmware': False,
            }
        )

    def get_setup(self):
        base_url = self.get_base_url()
        self.send_json_response(
            {
                'api_key': '123456789',
                'friendly_id': 'TRMNL123',
                'image_url': f'{base_url}/bitmap',
                'message': 'Welcome to trmnl_srv',
            }
        )

    def post_log(self):
        try:
            body = self.rfile.read(65536)
            text = body.decode('utf-8')
            logs = json.loads(text)
            self.log_message('Logs received:')
            formatted_logs = json.dumps(logs, indent=4, sort_keys=True)
            for line in formatted_logs.splitlines():
                self.log_message('%s', line)
            self.send_response(204)
            self.log_request(204)
        except Exception as exception:
            self.send_response(500)
            self.log_error('500 Error: %s', str(exception))

    def not_found(self):
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Not Found')
        self.log_error('404 Not Found: %s', self.path)

    def send_json_response(self, json_body: dict[str, Any] | list[Any]):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(json_body).encode('utf-8'))
        self.log_request(200)

    def log_request_details(self):
        self.log_message('Request details:')
        self.log_message('    %s', self.requestline)
        for key, value in sorted(self.headers.items()):
            self.log_message('    %s: %s', key, value)


class Server(HTTPServer):
    def __init__(self, host: str, port: int, content_file: Path):
        self.allow_reuse_address = True
        self.allow_reuse_port = True
        super().__init__((host, port), Handler)
        self.content_file = content_file


print('Serving...')

content_dir = Path('../tmp')
content_dir.mkdir(parents=True, exist_ok=True)
content_file = content_dir / 'content.bmp'
content_file2 = content_dir / 'content.png'

server = None
try:
    server = Server('', 4001, content_file)
    server.serve_forever()
except KeyboardInterrupt:
    server and server.server_close()
except Exception as e:
    print(e)
    sys.exit(1)

sys.exit(0)
