import sqlite3

con = sqlite3.connect('phonebook_try_1/phonebook')
cur = con.cursor()

class PhoneInfo:
    # 생성자
    def __init__(self, name, phonenumber, birthyear):
        self.name=name
        self.phonenumber=phonenumber
        self.birthyear=birthyear

    # 정보 출력하는 메서드
    def showinfo(self):
        print('--- <정보 출력> ---')
        print('이름 :', self.name, sep='\t')
        print('전화번호 :', self.phonenumber, sep='\t')
        print('생일 :', self.birthyear, sep='\t')

# 이름 비교후 동일 여부 결과 반환하는 메서드
    def checkInfo(self, keyword):
        return self.name==keyword

# __str__() 함수 재정의
def __str__(self):
    return '--- <정보 출력> --- \n이름 : {}\n전화번호 :{}\n생년 :{}'.format(self.name, self.phonenumber, self.birthyear)



def insertMember():
    name = input('이름을 입력해주세요 >>>')
    pNum = input('전화번호를 입력해주세요 >>>')
    bYear = input('생일을 입력해주세요 >>>')

    sql_insert = 'insert into user_pb_table values(\'{}\', {}, {})'.format(name, pNum, bYear)
    cur.execute(sql_insert)
    con.commit()
 

def showList():
    sql_select = 'select * from user_pb_table'
    cur.execute(sql_select)
    print('이름\t전번\t생년')
    while True:
        row = cur.fetchone() 
        if row == None:
            break
        print('{}\t{}\t{}'.format(row[0], row[1], row[2]))


# def searchInfo():
#     print('---- <검색> ----')
#     keyword = input('이름을 입력해주세요 >>>')
#     chk_num = 0  # 검색 결과가 없을때 : 0, 있을때 : 1 이상
#     for member in pBooks:
#         if member.checkInfo(keyword):
#             member.showinfo()
#             chk_num += 1
#     if(chk_num==0):
#         print('찾으시는 정보가 없습니다')

#     sql_select = 'select * from user_pb_table where user=\'{}\''.format(keyword)
#     cur.execute(sql_select)

# def deleteInfo():
#     print('---- <삭제> ----')
#     keyword = input('이름을 입력해주세요 >>>')
#     delCnt = 0

#     for i, member in enumerate(pBooks):
#         if member.checkInfo(keyword):
#             del pBooks[i]
#             delCnt += 1
#     if(delCnt==0):
#         print('찾으시는 정보가 없습니다')

#con.close()