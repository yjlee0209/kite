# from urllib import request
# from bs4 import BeautifulSoup

# r = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=8YHI0PHJUP9EZ7S9")
# soup = BeautifulSoup(r, "html.parser")

# for fdata in soup.select('span'):
#     print(fdata.string)

from urllib import request
from bs4 import BeautifulSoup

t = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=6WM696GI9AM4L7VV")
soup_t = BeautifulSoup(t, "html.parser")

for t_data in soup_t.select('span'):
    print(t_data.string)

s = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=KNRNAD7LPGJXV55H")
soup_s = BeautifulSoup(s, "html.parser")

for s_data in soup_s.select('strong'):
    print(s_data.string)

d = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=07W76PN9B4DG848U")
soup_d = BeautifulSoup(d, "html.parser")

for d_data in soup_d.select('dd'):
    dust = int(d_data.span.string[:-3])
    print(dust)
    if 0<=dust<=30:
        print('좋음')
    elif 30<dust<=50:
        print('보통')
    elif 51<dust<=100:
        print('나쁨')
    elif 100<dust:
        print('매우나쁨')

md = request.urlopen("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=EV04SJAXT8EJK2OC")
soup_md = BeautifulSoup(md, "html.parser")

for md_data in soup_md.select('dd'):
    mdust = int(md_data.span.string[:-3])
    print(mdust)
    if 0<=mdust<=15:
        print('좋음')
    elif 15<mdust<=25:
        print('보통')
    elif 25<mdust<=50:
        print('나쁨')
    elif 50<mdust:
        print('매우나쁨')