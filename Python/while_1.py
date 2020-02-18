# list 선언

list_a = [1, 2, 1, 2, 2, 3, 4, 2, 4, 2, 1, 2, 2, 4, 2]
print(list_a)

list_a.remove(2)
print(list_a)

val = 2

while val in list_a:
    list_a.remove(val)

print(list_a)

