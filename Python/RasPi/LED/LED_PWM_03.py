# coding: utf-8

# GPIO
import RPi.GPIO as GPIO
import time
import tkinter as tk

# GPIO 핀번호 할당
GPIO.setmode(GPIO.BOARD)

# 핀(채널)번호 설정
LED_R = 11
LED_Y = 16
LED_G = 22

# 핀 설정
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_Y, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)

# PWM 객체 생성 : 11번 핀, 주파수 - 100Hz
p_r = GPIO.PWM(LED_R, 100)
p_y = GPIO.PWM(LED_Y, 100)
p_g = GPIO.PWM(LED_G, 100)

# PWM 신호 출력
p_r.start(0)
p_y.start(0)
p_g.start(0)

# window Obj
window = tk.Tk()
window.geometry('300x300')

# 변수 설정
led_r_value = tk.DoubleVar()
led_y_value = tk.DoubleVar()
led_g_value = tk.DoubleVar()

led_r_value.set(0)
led_y_value.set(0)
led_g_value.set(0)

# duty 값을 변경 함수
def change_duty_r(dc):
    p_r.ChangeDutyCycle(led_r_value.get())

def change_duty_y(dc):
    p_y.ChangeDutyCycle(led_y_value.get())

def change_duty_g(dc):
    p_g.ChangeDutyCycle(led_g_value.get())

# 슬라이드 객체 생성
# 레이블(LED 밝기 조정), 숫자 범위(0~100)
slide_r = tk.Scale(window, label='빨간 LED 밝기 조절', orient='h', from_=0, to=100, variable=led_r_value, command=change_duty_r)
slide_y = tk.Scale(window, label='노란 LED 밝기 조절', orient='h', from_=0, to=100, variable=led_y_value, command=change_duty_y)
slide_g = tk.Scale(window, label='초록 LED 밝기 조절', orient='h', from_=0, to=100, variable=led_g_value, command=change_duty_g)

slide_r.pack()
slide_y.pack()
slide_g.pack()

window.mainloop()

# PWM 정지
p_r.stop()
p_y.stop()
p_g.stop()

# GPIO 개방
GPIO.cleanup()