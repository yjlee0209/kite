# 데이터 저장용 list 선언, 데이터 입력
# students = [
#     {'name':'scott', 'korean':87, 'math':93, 'english':96, 'science':36},
#     {'name':'king', 'korean':55, 'math':90, 'english':36, 'science':70},
#     {'name':'adam', 'korean':77, 'math':95, 'english':47, 'science':69},
#     {'name':'smith', 'korean':83, 'math':20, 'english':67, 'science':47},
#     {'name':'son', 'korean':81, 'math':56, 'english':87, 'science':58},
#     {'name':'lee', 'korean':97, 'math':76, 'english':96, 'science':58},
#     {'name':'kim', 'korean':34, 'math':36, 'english':74, 'science':47}
# ]

# Student Class 정의
class Student:
    # Constructor 정의
    def __init__(self, name, kor, math, eng, sci):
        self.name=name
        self.korean=kor
        self.math=math
        self.english=eng
        self.science=sci        
    
    # 각 과목의 점수의 합을 수해 반환하는 메서드
    def score_sum(self):
        return self.korean +self.math +self.english +self.science
    
    # 각 과목의 평균값을 구해 반환하는 메서드
    def score_avg(self):
        return self.score_sum()/4


# class를 이용한 인스턴스 생성
# st_a = Student()
# print(type(st_a))
# st_a.name = 'son'  # st_a 객체에 name 속성을 동적 추가
# print(st_a.name)

# st_b = Student()
# print(type(st_b))
# print(st_b.name)

# 1. list의 추가할 Object를 만드는 함수
def makeStudent(name, kor, math, eng, sci):
    return{
        'name': name,
        'korean': kor, 
        'math': math, 
        'english': eng, 
        'science': sci
    }

# 2. list의 추가할 Object를 class를 이용해서 만드는 함수
# def makeStudent_class(name, kor, math, eng, sci):
#     st_temp = Student()
#     st_temp.name = name
#     st_temp.korean = kor
#     st_temp.math = math
#     st_temp.english = eng
#     st_temp.science = sci
#     return st_temp


# students = [
#     makeStudent_class('Kim', 87, 93, 96, 36),
#     makeStudent_class('Lee', 55, 90, 36, 70),
#     makeStudent_class('Park', 77, 95, 47, 69),
#     makeStudent_class('Choi', 83, 20, 67, 47),
#     makeStudent_class('Jeong', 81, 56, 87, 58),
#     makeStudent_class('Son', 97, 76, 96, 58),
#     makeStudent_class('Ryu', 34, 36, 74, 47)
# ]

# Student class를 이용한 object 생성
students = [
    Student('Kim', 87, 93, 96, 36),
    Student('Lee', 55, 90, 36, 70),
    Student('Park', 77, 95, 47, 69),
    Student('Choi', 83, 20, 67, 47),
    Student('Jeong', 81, 56, 87, 58),
    Student('Son', 97, 76, 96, 58),
    Student('Ryu', 34, 36, 74, 47)
]

# 학생들의 이름, 총점, 평균
print('이름', '총점', '평균', sep='\t')

# 학생 리스트 반복 출력
for st in students:
    # dic 참조
    #score_sum = st['korean'] +st['english'] +st['math'] +st['science']
    # class instance 속성 참조
    #score_sum = st.korean +st.english +st.math +st.science
    #score_avg = score_sum/4
    #print(st['name'], score_sum, score_avg, sep='\t' )
    #print(st.name, score_sum, score_avg, sep='\t')
    print(st.name, st.score_sum(), st.score_avg(), sep='\t')