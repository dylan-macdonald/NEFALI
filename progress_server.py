#!/usr/bin/env python3
"""Simple progress server for NEFALI cross-model analysis."""

import http.server
import socketserver
import json
import os
from pathlib import Path

PORT = 8765
PROGRESS_FILE = Path(__file__).parent / "analysis_progress.json"

class ProgressHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/progress':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            if PROGRESS_FILE.exists():
                data = PROGRESS_FILE.read_text()
            else:
                data = json.dumps({"status": "waiting", "message": "Analysis not started yet"})

            self.wfile.write(data.encode())
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html_path = Path(__file__).parent / "dashboard.html"
            if html_path.exists():
                self.wfile.write(html_path.read_bytes())
            else:
                self.wfile.write(b"<h1>Dashboard not found</h1>")
        else:
            super().do_GET()

    def log_message(self, format, *args):
        pass  # Suppress logging

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ProgressHandler) as httpd:
        print(f"Progress dashboard running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()
