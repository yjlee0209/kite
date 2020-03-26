from urllib import request
from bs4 import BeautifulSoup

r = request.urlopen('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=KNRNAD7LPGJXV55H')
soup = BeautifulSoup(r, 'html.parser')

for t_data in soup.select('strong'):
    print(t_data.string)