# Student Class 정의
class Student:
    count = 0
    # Constructor 정의
    def __init__(self, name, kor, math, eng, sci):
        self.name=name
        self.korean=kor
        self.math=math
        self.english=eng
        self.science=sci

        Student.count += 1
        print('인스턴스가 생성되었습니다.')

    # 각 과목의 점수의 합을 수해 반환하는 메서드
    def score_sum(self):
        return self.korean +self.math +self.english +self.science
    
    # 각 과목의 평균값을 구해 반환하는 메서드
    def score_avg(self):
        return self.score_sum()/4

    # __str__() 재 정의
    def __str__(self):
        return '{}\t{}\t{}'.format(self.name, self.score_sum(), self.score_avg())

    @classmethod
    def print(cls):
        print(Student.count)

Student.print()

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

print('{}개의 리스트의 요소가 생성되었습니다'.format(Student.count))

# 학생들의 이름, 총점, 평균
print('이름', '총점', '평균', sep='\t')

# 학생 리스트 반복 출력
for st in students:
    #print(st.name, st.score_sum(), st.score_avg(), sep='\t')
    print(st)