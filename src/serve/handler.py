import email.utils
import json

from common.logs.trmnl_log_entry import TRMNLLogEntry
from http.server import BaseHTTPRequestHandler
from pathlib import Path

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
            case '/logs':
                self.__get_logs()
            case _:
                if self.path.startswith('/logs/'):
                    self.__get_log_file()
                else:
                    self.not_found()
        self.log_request_details()

    def do_POST(self):
        match self.path:
            case '/api/log':
                self.__post_log()
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
        self.__writeln('<!doctype html>')
        self.__writeln('<html lang=en>')
        self.__writeln('<title>trmnl_srv</title>')
        self.__writeln('<main>')
        self.__writeln('    <h1>trmnl_srv</h1>')
        self.__writeln('    <ul>')
        self.__writeln('        <li><p></p><a href=/api/setup>/api/setup</a>')
        self.__writeln('        <li><p><a href=/api/display>/api/display</a>')
        self.__writeln('        <li><p><a href=/content>/content</a>')
        self.__writeln('        <li><p><a href=/content/bitmap>/content/bitmap</a>')
        self.__writeln('        <li><p><a href=/logs>/logs</a>')
        self.__writeln('    </ul>')
        self.__writeln('</main>')

    def __get_logs(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.__writeln('<!doctype html>')
        self.__writeln('<html lang=en>')
        self.__writeln('<title>TRMNL logs</title>')
        self.__writeln('<main>')
        self.__writeln('    <h1>TRMNL logs</h1>')
        self.__writeln('    <ul>')
        for path in sorted(self.server.logs_dir.iterdir(), reverse=True):
            rel_path = path.relative_to(self.server.logs_dir.parent)
            self.__writeln(f'        <li><p><a href={rel_path}>{path.name}</a>')
        self.__writeln('    </ul>')
        self.__writeln('</main>')

    def __post_log(self):
        try:
            self.send_response(204)
            self.end_headers()
            buffer_size = 16384
            body = self.rfile.read1(buffer_size)
            if len(body) == buffer_size:
                self.log_message('Error: buffer overflow while reading POST to /api/log')
            self.__write_log_messages(body)
        except Exception as exception:
            self.send_response(500)
            self.log_error('500 Error: %s', str(exception))

    def not_found(self):
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Not Found')
        self.log_error('404 Not Found: %s', self.path)

    def log_request_details(self):
        self.log_message('    %s', self.requestline)
        for key, value in sorted(self.headers.items()):
            self.log_message('    %s: %s', key, value)

    def __get_json_file(self, path: Path):
        if not path.exists():
            self.__service_unavailable()
            return

        last_modified = path.stat().st_mtime

        with path.open('r') as f:
            json_object = json.load(f)

        json_text = json.dumps(json_object, indent='    ', sort_keys=True)
        body = json_text.encode('utf-8')
        content_length = len(body)

        self.send_response(200)
        self.send_header('Content-Length', str(content_length))
        self.send_header('Content-Type', 'application/json')
        self.send_header(
            'Last-Modified',
            email.utils.formatdate(last_modified, localtime=False, usegmt=True),
        )
        self.end_headers()
        self.wfile.write(body)

    def __get_log_file(self):
        rel_path = Path(self.path[1:]) if self.path.startswith('/') else self.path
        path = self.server.web_root.joinpath(rel_path)
        if not path.exists():
            self.not_found()
            return

        last_modified = path.stat().st_mtime

        with path.open('r') as f:
            log_file = f.read()

        body = log_file.encode('utf-8')
        content_length = len(body)

        self.send_response(200)
        self.send_header('Content-Length', str(content_length))
        self.send_header('Content-Type', 'application/json')
        self.send_header(
            'Last-Modified',
            email.utils.formatdate(last_modified, localtime=False, usegmt=True),
        )
        self.end_headers()
        self.wfile.write(body)

    def __service_unavailable(self):
        self.send_response(503)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Service Unavailable')
        self.log_error('503 Service Unavailable')

    def __writeln(self, line: str):
        self.wfile.write(line.encode())
        if not line.endswith('\n'):
            self.wfile.write('\n'.encode())

    def __write_log_messages(self, log_body: bytes):
        try:
            entries = TRMNLLogEntry.get_entries(self.server.trmnl_logs.path, log_body)
            entries.sort(key=lambda entry: entry.log_id)
            for entry in entries:
                if not entry.path.exists():
                    entry.write()
                    self.log_message(f'Log ID {entry.log_id}: {entry.log_message}')
        except Exception as e:
            self.log_error(f'Error parsing POST /api/log request: {e}')
