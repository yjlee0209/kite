import pb_manager as pbm
import sys

while True:
    print('메뉴를 입력해주세요!\n (1) 입력 \n (2) 출력 \n (3) 검색 \n (4) 삭제 \n (5) 종료')
    choice = input('메뉴 번호를 입력해주세요 >>>')
    if choice == '1':
        pbm.insertMember()
    elif choice == '2':
        pbm.showList()
    # elif choice == '3':
    #     pbm.searchInfo()
    # elif choice == '4':
    #     pbm.deleteInfo()
    elif choice == '5':
        #break
        sys.exit()
    else:
        print('유효한 번호가 아닙니다. 다시 입력해주세요')