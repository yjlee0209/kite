## coding: utf-8

from urllib.request import urlopen, Request
import urllib
import bs4

## 검색할 장소 입력
##loc_input = str(input('장소를 입력해 주세요 >> '))

loc = '서울시'   ##loc_input
loc_a = urllib.parse.quote(loc + '+날씨')

## 요청할 주소
url = 'https://search.naver.com/search.naver?ie=utf8&query='+ loc_a

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html5lib')

## 검색된 정보 출력
#print('현재 ' + loc + '의 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.')
print('Current temp of Seoul is ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text)