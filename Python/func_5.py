# 빈 리스트 선언
list_a = []

# 반복문을 이용한 데이터 추가
for i in range(0,20,2):
    list_a.append(i*i)
print('A=',list_a)

list_b = [i*i for i in range(0,20,2) if i > 10]
print('B=',list_b)

array = ['사과', '자두', '바나나', '체리', '초콜릿']
output = [ f for f in array if f != '초콜릿']
print(array)
print(output)