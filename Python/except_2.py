list_ex = ['52', '324', '435', '스파이', '13']

list_result = []

for item in list_ex:
    try:
        float(item)
    except Exception as e:
        #pass
        print('type(e) :',type(e))
        print('Exception e :', e)
    else:
        list_result.append(item)
    finally:
        print('한번의 반복 구문이 완료되었습니다')

print(list_ex)
print(list_result)