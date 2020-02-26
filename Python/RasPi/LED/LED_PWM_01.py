# coding: utf-8

# GPIO
import RPi.GPIO as GPIO
import time

# GPIO 핀번호 할당
GPIO.setmode(GPIO.BOARD)

# 핀(채널)번호 설정
LED_R = 11
LED_Y = 16
LED_G = 22

# 밝기 목록 (0.0 ~ 100.0)
dc = [0,1,2,3,4,5,6,7,8,9,10,12,13,15,20,30,50,70,100]

# 핀 설정
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_Y, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)

# PWM 객체 생성 : 11번 핀, 주파수 - 100Hz
p_r = GPIO.PWM(LED_R, 100)
p_y = GPIO.PWM(LED_Y, 100)
p_g = GPIO.PWM(LED_G, 100)

# PWM 신호 출력
p_r.start(80)
p_y.start(20)
p_g.start(50)
time.sleep(1)
p_r.start(20)
p_y.start(50)
p_g.start(80)
time.sleep(1)
p_r.start(50)
p_y.start(80)
p_g.start(20)
time.sleep(1)


# PWM 정지
p_r.stop()
p_y.stop()
p_g.stop()

# GPIO 개방
GPIO.cleanup()