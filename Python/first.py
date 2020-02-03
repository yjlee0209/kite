print("First Python") # print 실행

# 기본 내장 함수

# abs
print("   <<절대값 abs() 함수>>")
print(abs(5))
print(abs(-5))


#max
print("   <<최대값 max() 함수>>")
print(max([1,2,3]))
print(max([1,2,3],[4,5,6]))

a = 10
b = 20
nums1 = [10,40,100,60,30]
nums2 = [10,40,100,60,50]
names = "python"  # 문자열
print(max(a,b))
print(max(nums1))
print(max(nums1,nums2))
print(max(names))


#mix
print("   <<최소값 min() 함수>>")
print(min([1,2,3]))
print(min([1,2,3],[4,5,6]))

a = 10
b = 20
nums1 = [10,40,100,60,30]
nums2 = [10,40,100,60,50]
names = "python"  # 문자열
print(min(a,b))
print(min(nums1))
print(min(nums1,nums2))
print(min(names))


#pow
print("   <<거듭제곱 pow() 함수>>")
print(pow(2,2))
print(pow(3,3))
print(pow(2,-1))


#chr
print("   <<chr() 함수>>")
print(chr(97))
print(chr(65))
print(chr(48))
print(chr(97+1))
print(chr(65+1))
print(chr(48+1))


#str
print("   <<문자열 str() 함수>>")
print(str(97))
print(str([10, 100, 30, 'hun']))
print(str("String"))


#range
print("   <<범위 range() 함수>>")
print(list(range(10)))
print(list(range(3, 10)))
print(list(range(3, 10, 2)))


#type
print("   <<자료형 반환 type() 함수>>")
print(type(-1))
print(type("word"))
print(type([1,2,3,4,5]))


#식별자 주의사항
#키워그, 함수이름, 모듈이름, 클래스이름 과 동일하게 사용하면 안된다.
print("   <<식별자 주의사항>>")
str = 'abc'  # 기존의 함수 str이 변수 str로 변경 : 오류가 아니다.
print(str)    # print(str('abc')) : 함수 호출 오류 발생


#문자열
print("   <<문자열>>")
print("동해물과 백두산이 마르고 닳도록")
print("""\
동해물과
백두산이
마르고
닳도록
""")    # \ : 불필요한 공백을 없에준다.

print("Python" *3)
print(4* "Python")

print("안녕하세요"[-5])
print("안녕하세요"[1:4])
print("안녕하세요"[4])

print("안녕하세요"[:2])
print("안녕하세요"[2:])

print(len("안녕하세요"))


#숫자 연산
print("   <<연산자>>")
print("5 + 7 =", 5+7)
print("5 - 7 =", 5-7)
print("5 * 7 =", 5*7)
print("7 / 5 =", 7/5)
print("7 // 5 =", 7//5)
print("7 % 5 =", 7%5)
print("2**1 =", 2**1)
print("2**2 =", 2**2)
print("2**4 =", 2**4)


#사용자 데이터 입력
print("   <<사용자 데이터 입력>>")
#age = input("나이를 입력해주세요 >>> ")
#print(type(age))    # 숫자를 입력해도 문자열로 반환한다.
#print(age)

#string_a = input("숫자를 입력해주세요 >>> ")
#string_b = input("다른 숫자를 입력해주세요 >>> ")
#int_a = int(string_a)
#int_b = int(string_b)
#print("문자열 연산 : ", string_a+string_b)
#print("숫자 연산 : ", int_a+int_b)


#문자열을 다루는 기본함수
string_str = "hello python"

string_a = "{}".format(20)
print(string_a)
print(type(string_a))

format_a = "{}만원".format(5000)
format_b = "파이썬 열공해서 첫 연봉 {}만원 만들기".format(5000)
format_c = "{}, {}, {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, '문자열', True)
print(format_a)
print(format_b)
print(format_c)
print(format_d)
print(type(format_d))