# coding: utf-8

# GPIO 모듈
import RPi.GPIO as GPIO
import tkinter as tkinter
import time

# 핀 번호 할당으로 처리 : 핀번호 설정
GPIO.setmode(GPIO.BOARD)

# 핀 번호 설정 : channel
LED_G = 11

# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0 False
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)

print('=====> LED_G : ', GPIO.input(LED_G))

def func():
    GPIO.output(LED_G, not GPIO.input(LED_G))
    time.sleep(3)

cnt = 0
while 1:
    if(cnt > 10):
        break
    func()
    print('=====> LED_G : ', GPIO.input(LED_G))
    cnt += 1

GPIO.cleanup()