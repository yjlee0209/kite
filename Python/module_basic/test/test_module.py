# 변수 
PI = 3.14

# 함수 : 사용자의 데이터 입력 값을 반환하는 기능
def number_input():
    result = input('숫자를 입력해주세요 >>> ')
    return float(result)

# 함수 : 원의 둘레를 구하고 값을 반환하는 기능
def get_circumference(radius):
    return 2*PI*radius

# 함수 : 원의 면적을 구해서 반환하는 기능
def get_circle_area(radius):
    return PI*radius*radius

print(__name__)