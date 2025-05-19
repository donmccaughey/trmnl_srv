from http.server import HTTPServer
from pathlib import Path



class Server(HTTPServer):
    def __init__(self, host: str, port: int, web_root: Path):
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
