# coding: utf-8

# GPIO 라이브러리 호출
import RPi.GPIO as GPIO

# time 모듈
import time

# 핀 번호로 제어 : 핀 번호 할당 -> 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

LED_R = 11
LED_Y = 16
LED_G = 22

GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_Y, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)

def func_clear():
    GPIO.output(LED_R, False)
    GPIO.output(LED_Y, 0)
    GPIO.output(LED_G, GPIO.LOW)

def func_r():
    func_clear()
    GPIO.output(LED_R, not GPIO.input(LED_R))
    time.sleep(3)

def func_y():
    func_clear()
    cnt_y = 0
    while 1:
        if(cnt_y > 3):
            break
        cnt_y += 1
        GPIO.output(LED_Y, not GPIO.input(LED_Y))
        time.sleep(0.5)
        GPIO.output(LED_Y, not GPIO.input(LED_Y))
        time.sleep(0.5)

def func_g():
    func_clear()
    GPIO.output(LED_G, not GPIO.input(LED_G))
    time.sleep(3)

cnt = 0

while 1:
    if(cnt > 2):
        break
    cnt += 1
    func_r()
    func_y()
    func_g()

# GPIO 개방
GPIO.cleanup()