from tkinter import *
from tkinter import messagebox
#tkinter : GUI 관련된 모듈

# 이벤트 함수 : 핸들러 함수
def myFunc(): 
    messagebox.showinfo('SALAD', '배고파!')

def check_func():
    if chk.get()==0:
        messagebox.showinfo('Checkbutton', '체크 상태가 아닙니다.')
    else:
        messagebox.showinfo('Checkbutton', '체크 상태입니다.')

def radio_func():
    if val.get()==1:
        label_c.configure(text='JAVA')
    elif val.get()==2:
        label_c.configure(text='Spring')
    elif val.get()==3:
        label_c.configure(text='Python')
    else:
        messagebox.showinfo('', '정상적인 입력 데이터가 아닙니다.')


# window 생성
window = Tk() # 윈도우 생성 반환

#윈도우 이름 설정
window.title('First Window')
#윈도우 사이즈 지정 : 폭x높이
window.geometry('400x600')
#윈도우의 사이즈 조정 여부 설정
window.resizable(width=TRUE, height=TRUE)

# 텍스프 표현을 위한 Label
# text : 화면에 표현할 텍스트
# font : 폰트 종류, 사이즈
# fg : 폰트 컬러
# bg : 배경색
# width, height : 텍스트 표현 영역(너비, 높이)
# anchor : 영역 내의 텍스트 표현 위치
label_a = Label(
    window, 
    text='Python', 
    font=('궁서체', 20), 
    fg='red', 
    bg='yellow', 
    width=26, 
    height=7, 
    anchor=NW)

label_b = Label(
    window, 
    text='파이선', 
    font=('궁서체', 20), 
    fg='red', 
    bg='yellow', 
    width=26, 
    height=7, 
    anchor=NW)

label_c = Label(
    window, 
    text='원도우', 
    font=('궁서체', 20), 
    fg='red', 
    bg='yellow', 
    width=26, 
    height=4, 
    anchor=NW)

#이미지 위젯 : 이미지 표현
#photo = PhotoImage(file='image/hamburger.jpg')
photo = PhotoImage(file='image/salad.png')
label_photo = Label(window, image=photo, width=400, height=300, anchor=E)

#버튼 위젯 : 버튼 표현
btn_close = Button(window, text='종료', fg='blue', bg='yellow', command=quit)
#이미지 버튼 처리, 이벤트 핸들러 함수 이용
btn_img = Button(window, image=photo, command=myFunc)

#체크 박스 : Checkbutton
chk = IntVar()
check_btn_a = Checkbutton(window, text='체크해주세요.', variable=chk, command=check_func)

#레디오 버튼 : Radiobutton
val = IntVar()
radio_btn_a = Radiobutton(window, text='JAVA', variable=val, value=1, command=radio_func)
radio_btn_b = Radiobutton(window, text='Spring', variable=val, value=2, command=radio_func)
radio_btn_c = Radiobutton(window, text='Python', variable=val, value=3, command=radio_func)

#원도우 위젯 배치
label_c.pack()
#label_a.pack()
#label_b.pack()
#label_photo.pack()
radio_btn_a.pack()
radio_btn_b.pack()
radio_btn_c.pack()
check_btn_a.pack()
btn_img.pack()
btn_close.pack()

# window 출력
window.mainloop()