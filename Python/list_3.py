# list 선언
list_a = [1, 2, 3]
list_b = [1, 2, 1, 2]

# list에 요소 추가 : append -> 마지막 index 뒤로 추가
list_a.append(4)
print(list_a)
list_a.append(5)
print(list_a)

# list에 요소 추가 : insert -> 특정 index의 위치에 추가
list_a.insert(0,0)
print(list_a)
list_a.insert(2,6)
print(list_a)

# list 다른 list 요소를 추가 : extend
list_a.extend([10,20,30])
print(list_a)

# list 요소 삭제 : del
del list_a[5]
print(list_a)

list_a.pop(7)
print(list_a)

# list 요소 범위 삭제
del list_a[2:5]
print(list_a)

del list_a[3:]
print(list_a)

# list 특정값 삭제 : remove
list_a.remove(5)
list_b.remove(2)
print(list_a)
print(list_b)

# list 모든 요소 삭제 : clear
list_b.clear()
print(list_b)

# list 요소 존제 유무 확인 : in
chk_1 = 1 in list_a
chk_2 = 2 in list_a
print('list_a의 요소에 1이 존재 하는가?  >>> ', chk_1)
print('list_a의 요소에 2가 존재 하는가?  >>> ', chk_2)