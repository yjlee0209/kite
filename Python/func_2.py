# list 선언
list_a = [1,2,3,4,5,6]
list_b = list(range(1,7))

print('A=',list_a)
print('B=',list_b)

# list 역순으로
list_reversed = reversed(list_a)
list_reversed = list(list_reversed)
print('A*=',list_reversed)

# for 문장을 이용해서 역순 참조
for i in reversed(list_a):
    print(i)