#!/usr/bin/env python3
"""
Simple local development server for Dai Nam GDQP-AN Presentation.
Run with: python scripts/serve.py
Then open http://localhost:8000 in your browser.
"""
import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).resolve().parent.parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

def main():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"==================================================")
        print(f"  DAI NAM UNIVERSITY - GDQP-AN PRESENTATION SERVER")
        print(f"  Serving at: {url}")
        print(f"  Root: {DIRECTORY}")
        print(f"  Press Ctrl+C to stop the server.")
        print(f"==================================================")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
