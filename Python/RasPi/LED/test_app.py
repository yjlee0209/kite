# coding: utf-8

# flask 
from flask import Flask
# requestparam
from flask import request
# CORS
from flask_cors import CORS

import RPi.GPIO as GPIO

######################################################################

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

# duty 값을 변경 함수
def change_duty_r(dc):
    p_r.ChangeDutyCycle(dc)

def change_duty_y(dc):
    p_y.ChangeDutyCycle(dc)

def change_duty_g(dc):
    p_g.ChangeDutyCycle(dc)



######################################################################

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():

    led_1 = request.args.get('led_1', 'r')
    p_r_val = request.args.get('p_r_val', '0')
    led_2 = request.args.get('led_2', 'y')
    p_y_val = request.args.get('p_y_val', '0')
    led_3 = request.args.get('led_3', 'g')
    p_g_val = request.args.get('p_g_val', '0')

    change_duty_r(int(p_r_val))
    change_duty_y(int(p_y_val))
    change_duty_g(int(p_g_val))

    return led_1 + ' : ' + p_r_val + '<br>' + led_2 + ' : ' + p_y_val + '<br>' + led_3 + ' : '+ p_g_val  

if __name__ == '__main__':
    app.run(host='192.168.0.67', port='5000')