import json

from http.server import BaseHTTPRequestHandler
from typing import Any

from .server import Server


class Handler(BaseHTTPRequestHandler):
    server: Server

    def do_GET(self):
        self.log_request_details()
        match self.path:
            case '/':
                self.get_index()
            case '/api/display':
                self.get_display()
            case '/api/setup':
                self.get_setup()
            case '/content':
                self.get_content()
            case '/content/bitmap':
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
        self.send_header('Content-Type', 'image/png')
        self.end_headers()
        with self.server.bitmap_file.open('rb') as f:
            self.wfile.write(f.read())
        self.log_request(200)

    def get_content(self):
        with self.server.content_file.open('r') as f:
            content = json.load(f)
            self.send_json_response(content)

    def get_display(self):
        with self.server.api_display_file.open('r') as f:
            display = json.load(f)
            self.send_json_response(display)

    def get_index(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        page = '\n'.join([
            '<!doctype html>',
            '<html lang=en>',
            '<title>trmnl_srv</title>',
            '<main>',
            '    <h1>trmnl_srv</h1>',
            '    <ul>',
            '        <li><p></p><a href=/api/setup>/api/setup</a>',
            '        <li><p><a href=/api/display>/api/display</a>',
            '        <li><p><a href=/content>/content</a>',
            '        <li><p><a href=/content/bitmap>/content/bitmap</a>',
            '    </ul>',
            '</main>',
        ])
        self.wfile.write(page.encode())

    def get_setup(self):
        with self.server.api_setup_file.open('r') as f:
            setup = json.load(f)
            self.send_json_response(setup)

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
        self.wfile.write(json.dumps(json_body, indent='    ', sort_keys=True).encode('utf-8'))
        self.log_request(200)

    def log_request_details(self):
        self.log_message('Request details:')
        self.log_message('    %s', self.requestline)
        for key, value in sorted(self.headers.items()):
            self.log_message('    %s: %s', key, value)
