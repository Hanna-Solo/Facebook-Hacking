from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests


parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
url = "http://www.facebook.com"
resp = requests.get(url)
http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(resp.content, parser, from_encoding=encoding)
img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]
for url in urls:
    print(url)

for link in soup.find_all('a', href=True):
    print(link['href'])



