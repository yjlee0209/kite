# Bool 타입으로 치환되는 상황
# 0 -> False
# None -> False
# 빈 문자열 -> False
# 빈 리스트 -> False

num = 10
str_blank = "asd"
nums = [1,2,3]

if num:
    print('0은 True 처리가됩니다.')
else:
    print('0은 False 처리가됩니다.')

if str_blank:
    print('빈 문자열은 True 처리가됩니다.')
else:
    print('빈 문자열은 False 처리가됩니다.')

if nums:
    print('빈 리스트는 True 처리가됩니다.')
else:
    print('빈 리스트는 False 처리가됩니다.')
