#!/usr/bin/env python3
"""
Simple HTTP server for the Dragon Priestess Mermaid School landing page
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

PORT = 8888

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def main():
    # Change to the directory containing this script
    os.chdir(Path(__file__).parent)
    
    # Check if index.html exists
    if not os.path.exists('index.html'):
        print("❌ Error: index.html not found in current directory")
        sys.exit(1)
    
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"🌟 Dragon Priestess Mermaid School server starting...")
            print(f"🔮 Serving at http://localhost:{PORT}")
            print(f"✨ Opening mystical portal in your browser...")
            print(f"🐉 Press Ctrl+C to close the temple gates")
            
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print(f"\n🌸 Temple gates closing gracefully...")
        print(f"💖 May your path be luminous, beloved!")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Try a different port or close other servers.")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
