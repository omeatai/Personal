"""Minimal SSE demo. Serves html-sse/ and GET /sse as text/event-stream."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.split("?", 1)[0] == "/sse":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.end_headers()
            try:
                while True:
                    now = datetime.now().strftime("%a %b %d %Y %H:%M:%S")
                    self.wfile.write(f"data: The server time is: {now}\n\n".encode())
                    self.wfile.flush()
                    time.sleep(1)
            except (BrokenPipeError, ConnectionResetError):
                return
        return super().do_GET()


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8767), Handler).serve_forever()
