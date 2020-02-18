from bs4 import BeautifulSoup as bs
from urllib import request

# urlopen() 함수를 이용해서 기상청 데이터 가져오기
target = request.urlopen('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1165051000')
#data = target.read()
#print(data)
soup = bs(target, 'html.parser')

print(soup.find('title').string)

for fdata in soup.find_all('data'):
    print(fdata.hour.string, '시 예보, ', end='')
    print(fdata.day.string, '#, ', end='')    # 0:오늘, 1:내일, 2:모래
    print('현재 온도는 :', fdata.temp.string, '도, ', end='')
    print('강수 상태 :', fdata.pty.string)

