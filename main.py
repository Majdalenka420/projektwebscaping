import requests
import re

x = requests.get('https://godzilla.fandom.com/wiki/Godzilla_(disambiguation)')
headers = re.findall('h3.*?h3', x.text)
for head in headers:
    print("\n") 
    print(head)
