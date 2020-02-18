# dtetime 모듈 읽기
import datetime

# 현재 날자, 시간 정보
now = datetime.datetime.now()

# 시간 출력 : 포맷팅

output_a = now.strftime('%Y.%m.%d. %H:%M:%S')
output_a1 = now.strftime('%Y년%m월%d일 %H시%M분%S초')
output_b = '{}년 {}월 {}일 {}시{}분{}초'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
output_c = now.strftime('%Y{}%m{}%d{} %H{}%M{}%S{}'.format(*'년월일시분초'))
print(output_a)
print(output_a1)
print(output_b)
print(output_c)

# 특정 시간
print('-- <datetime.timedelta 시간 더하기> --')
after_a = now + datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
output_d = after_a.strftime('%Y{}%m{}%d{} %H{}%M{}%S{}'.format(*'년월일시분초'))
print(output_d)

# datime.replace 를 통해서 특정 시간 요소 변경
print('-- <datime.replace 를 통해서 특정 시간 요소 변경> --')
after_b = now.replace(hour=(now.hour+3))
output_e = after_b.strftime('%Y{}%m{}%d{} %H{}%M{}%S{}'.format(*'년월일시분초'))
print(output_e)