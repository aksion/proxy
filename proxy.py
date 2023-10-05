import http.server
import socketserver
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
from dotenv import dotenv_values


env_vars = dotenv_values()
proxy_host = env_vars['PROXY_HOST']
proxy_port = int(env_vars['PROXY_PORT'])
base_url = env_vars['BASE_URL']
symbol = env_vars['SYMBOL']


class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def modify_content(self, tag):
        modified_text = re.sub(r'\b\w{6}\b', lambda x: x.group() + symbol, tag)
        return tag.replace_with(modified_text)

    def do_GET(self):
        requested_url = self.path

        try:
            full_url = urllib.parse.urljoin(base_url, requested_url)

            with urllib.request.urlopen(full_url) as response:
                response_headers = response.info()

                self.send_response(200)
                for header_key, header_value in response_headers.items():
                    self.send_header(header_key, header_value)
                self.end_headers()

                response_content = response.read().decode('utf-8')
                soup = BeautifulSoup(response_content, 'html.parser')

                for tag in soup.find_all(text=True):
                    self.modify_content(tag)

                modified_content = str(soup)

                self.wfile.write(modified_content.encode('utf-8'))

        except urllib.error.URLError as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Error: ' + str(e).encode())


with socketserver.TCPServer((proxy_host, proxy_port), ProxyHandler) as server:
    print(f'Proxy server is running on http://{proxy_host}:{proxy_port}')
    server.serve_forever()
