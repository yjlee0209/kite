# if_3.py  ->  if_4.py else문으로 개선
# 양의 정수 입력 받기
number = input('양의 정수를 입력해주세요 >>> ')
# 정수형 데이터로 형변환
int_num = int(number)

if int_num>0:
    # 마지막 자리수 축출
    last_char = number[-1]    # 1004 -> 4
    # 짝수
    if last_char in '02468':
        print('짝수입니다.')
    else:
        print('홀수입니다.')
    if int_num%2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')
    
    # 음수
    #if last_char in '13579':
    #    print('홀수입니다.')
    #if int_num%2 == 1:
    #    print('홀수입니다.')

else:
    print('양의 정수가 아닙니다. 프로그램을 종료합니다.')
#if int_num<1:
#    print('양의 정수가 아닙니다. 프로그램을 종료합니다.')