# coding: utf-8

# GPIO 모듈
import RPi.GPIO as GPIO
import tkinter as tk
import time

# 핀 번호 할당으로 처리 : 핀번호 설정
GPIO.setmode(GPIO.BOARD)

# 핀번호 설정 : chanel
LED_R = 11
LED_Y = 16
LED_G = 22

# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0  False
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
# 16번 핀 출력 핀으로 등록    
GPIO.setup(LED_Y, GPIO.OUT, initial=GPIO.LOW) 
# 22번 핀 출력 핀으로 등록    
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)


# 전channel의 값을 0으로 / False, 0, GPIO.LOW 같은 뜻
def func_clear():
    GPIO.output(LED_R, False)
    GPIO.output(LED_Y, 0)
    GPIO.output(LED_G, GPIO.LOW)
    btn_r.configure(text='빨간 LED ON!!')
    btn_y.configure(text='노란 LED ON!!')
    btn_g.configure(text='초록 LED ON!!')

def func_r():
    if GPIO.input(LED_R):    # 1: on
        btn_r.configure(text='빨간 LED ON!!')
    else:                    # 0: off    
        func_clear()
        btn_r.configure(text='빨간 LED OFF!!')
    
    GPIO.output(LED_R, not GPIO.input(LED_R))

    print('========> LED_R : ', GPIO.input(LED_R))
    
    
def func_y():
    if GPIO.input(LED_Y):    # 1: on
        btn_y.configure(text='노란 LED ON!!')
    else:                    # 0: off    
        func_clear()
        btn_y.configure(text='노란 LED OFF!!')
    
    GPIO.output(LED_Y, not GPIO.input(LED_Y))
    
    print('========> LED_Y : ', GPIO.input(LED_Y))
   

def func_g(): 
    if GPIO.input(LED_G):    # 1: on
        btn_g.configure(text='초록 LED ON!!')
    else:                    # 0: off    
        func_clear()
        btn_g.configure(text='초록 LED OFF!!')
    
    GPIO.output(LED_G, not GPIO.input(LED_G))  
   
    print('========> LED_W : ', GPIO.input(LED_G))
    

# 윈도우 객체
window = tk.Tk()
window.geometry('400x400')

# label 객체 생성
label = tk.Label(window, text='버튼을 눌러서 LED 점등을 하세요')

# button 객체 생성
btn_r = tk.Button(window, text='빨간 LED ON!!', command=func_r)
btn_y = tk.Button(window, text='노란 LED ON!!', command=func_y)
btn_g = tk.Button(window, text='초록 LED ON!!', command=func_g)

# 위젯 배치
label.pack()
btn_r.pack()
btn_y.pack()
btn_g.pack()

# 윈도우 출력
window.mainloop()

# GPIO 개방
GPIO.cleanup()