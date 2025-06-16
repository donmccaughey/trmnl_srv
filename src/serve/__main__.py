import sys

from .options import Options
from .server import Server


options = Options.parse()

print('Serving...')

server = None
try:
    server = Server('', options.port, options.web_root, options.trmnl_logs)
    server.serve_forever()
except KeyboardInterrupt:
    server and server.server_close()
except Exception as e:
    print(e)
    sys.exit(1)

sys.exit(0)
