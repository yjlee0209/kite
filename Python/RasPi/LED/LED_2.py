# coding: utf-8

# GPIO 모듈
import RPi.GPIO as GPIO
import tkinter as tk
import time

# 핀 번호 할당으로 처리 : 핀번호 설정
GPIO.setmode(GPIO.BOARD)

# 핀 번호 설정 : channel
LED_R = 11
LED_Y = 16
LED_G = 22

# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0 False
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_Y, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)

print('=====> LED_R : ', GPIO.input(LED_R))
print('=====> LED_Y : ', GPIO.input(LED_Y))
print('=====> LED_G : ', GPIO.input(LED_G))

def func_1():
    GPIO.output(LED_R, not GPIO.input(LED_R))

def func_2():
    GPIO.output(LED_Y, not GPIO.input(LED_Y))

def func_3():
    GPIO.output(LED_G, not GPIO.input(LED_G))


# 윈도우 객체
window = tk.Tk()
window.geometry('400x400')

# label 객체 생성
label = tk.Label(window, text='버튼을 눌러서 LED 점등을 하세요')
# button 객체 생성
btn_r = tk.Button(window, text='LED 켜기/끄기', command=func_1)
btn_y = tk.Button(window, text='LED 켜기/끄기', command=func_2)
btn_g = tk.Button(window, text='LED 켜기/끄기', command=func_3)


# 위젯 배치
label.pack()
btn_r.pack()
btn_y.pack()
btn_g.pack()

# 윈도우 출력
window.mainloop()

# GPIO 개방
GPIO.cleanup()