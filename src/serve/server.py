from common.logs import LogStorage
from http.server import HTTPServer
from pathlib import Path
from sys import stdout


class Server(HTTPServer):
    def __init__(
            self, host: str, port: int, web_root: Path, trmnl_logs: LogStorage
    ):
        from .handler import Handler

        super().__init__((host, port), Handler)

        self.allow_reuse_address = True
        self.allow_reuse_port = True

        api_dir = web_root / 'api'
        self.api_display_file = api_dir / 'display/index.json'
        self.api_setup_file = api_dir / 'setup/index.json'

        content_dir = web_root / 'content'
        self.content_file = content_dir / 'index.json'
        self.bitmap_file = content_dir / 'bitmap/index.png'

        self.web_root = web_root

        self.trmnl_logs = trmnl_logs

        stdout.write(f'Listening on {self.server_address[0]}:{self.server_port}\n')
        stdout.flush()
