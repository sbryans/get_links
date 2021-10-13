import requests
import re
from urllib.parse import urljoin

target_url = input("Enter the full target URI: \n")

def extract_links(url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))

href_link = extract_links(target_url)

for link in href_link:
        link = urljoin(target_url,link)
        print(link)
