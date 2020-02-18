# circle 클래스 생성
# 속성(변수) :  반지름 -> radius , 외부에서 속성을 참조하지 못 하도록 보호
# 기능(메서드) :  원의 둘레, 원의 넓이

import math

class Circle:
    #생성자
    def __init__(self, radius):
        self.__radius = radius

    #__radius의 getter
    @property
    def radius(self):
        return self.__radius

    #__radius의 setter
    @radius.setter
    def radius(self, value):
        self.__radius=value
    

    # getter : __radius
    def get_radius(self):
        return self.__radius
    
    # setter : __radius
    def set_radius(self, value):
        self.__radius=value

    # 둘레
    def get_circumference(self):
        return 2*math.pi*self.__radius

    # 넓이
    def get_cirarea(self):
        return math.pi*self.__radius*self.__radius

# 인스턴스 생성
c_1 = Circle(10)

# setter 메서드를 통해서 변수에 값을 대입
c_1.set_radius(30)
c_1.radius=50

# getter 메서드를 통해서 __radius 값을 반환
print('반지름 :', c_1.get_radius(), sep='\t')
print('반지름 :', c_1.radius, sep='\t')

# 둘레
print('원의 둘레 :', c_1.get_circumference())
# 넓이
print('원의 넓이 :', c_1.get_cirarea())