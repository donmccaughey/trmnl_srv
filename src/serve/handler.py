import json

from http.server import BaseHTTPRequestHandler
from pathlib import Path
from typing import Any

from .server import Server


class Handler(BaseHTTPRequestHandler):
    server: Server

    def do_GET(self):
        match self.path:
            case '/':
                self.get_index()
            case '/api/display':
                self.__get_json_file(self.server.api_display_file)
            case '/api/setup':
                self.__get_json_file(self.server.api_setup_file)
            case '/content':
                self.__get_json_file(self.server.content_file)
            case '/content/bitmap':
                self.get_bitmap()
            case _:
                self.not_found()
        self.log_request_details()

    def do_POST(self):
        self.log_request_details()
        match self.path:
            case '/api/log':
                self.post_log()
            case _:
                self.not_found()

    def get_bitmap(self):
        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.end_headers()
        with self.server.bitmap_file.open('rb') as f:
            self.wfile.write(f.read())
        self.log_request(200)

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

    def log_request_details(self):
        self.log_message('    %s', self.requestline)
        for key, value in sorted(self.headers.items()):
            self.log_message('    %s: %s', key, value)

    def __get_json_file(self, path: Path):
        if path.exists():
            with path.open('r') as f:
                self.send_json_response(json.load(f))
        else:
            self.not_found()
