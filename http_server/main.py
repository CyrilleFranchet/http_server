#!/usr/bin/env python
# coding : utf-8

# Created by PyCharm on 25/03/2022
# Filename : main.py

from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse


def main():
    class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'Forbidden!')

    parser = argparse.ArgumentParser(description='Small dummy HTTP server.')
    parser.add_argument('-i', '--ip', help='IP address to use', required=True)

    args = parser.parse_args()

    httpd = HTTPServer((args.ip, 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
