from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('음식 선택')
window.geometry('500x500')

# handler function
def view_func(): 
    if check_val.get()==1:
        messagebox.showinfo('', '햄버거를 선택하셨군요!!')
    elif check_val.get()==2:
        messagebox.showinfo('', '피자를 좋아하시는군요!!')
    elif check_val.get()==3:
        messagebox.showinfo('', '치킨엔 맥주죠!!')
    else:
        messagebox.showinfo('', '잘못된 선택입니다!!')

# 화면구성을 위한 위젯

label_title = Label(text='좋아하는 음식을 선택해주세요!!!', font=('궁서체', 20), fg='blue')


# radio 선택 값을 저장할 변수
check_val = IntVar()
radio_btn_1 = Radiobutton(window, text='햄버거', variable=check_val, value=1)
radio_btn_2 = Radiobutton(window, text='피자', variable=check_val, value=2)
radio_btn_3 = Radiobutton(window, text='치킨', variable=check_val, value=3)

btn = Button(window, text='확인', command=view_func)



# 위젯 배치
label_title.pack()

radio_btn_1.pack()
radio_btn_2.pack()
radio_btn_3.pack()

btn.pack()


window.mainloop()