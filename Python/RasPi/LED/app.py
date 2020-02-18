# coding: utf-8

# flask
from flask import Flask

from flask_cors import CORS

# GPIO 모듈
import RPi.GPIO as GPIO

# 핀번호 할당
GPIO.setmode(GPIO.BOARD)

# 핀(채널)번호
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
    if not GPIO.input(LED_R):
        func_clear()

    GPIO.output(LED_R, not GPIO.input(LED_R))

    return str(GPIO.input(LED_R))
    
def func_y():
    if not GPIO.input(LED_Y):
        func_clear()
    
    GPIO.output(LED_Y, not GPIO.input(LED_Y))

    return str(GPIO.input(LED_Y))

def func_g(): 
    if not GPIO.input(LED_G):
        func_clear()
    
    GPIO.output(LED_G, not GPIO.input(LED_G))

    return str(GPIO.input(LED_G))




###########################################################################


app = Flask(__name__)

CORS(app)

@app.route('/sw_r')
def sw_r():
    return func_r()

@app.route('/sw_y')
def sw_y():
    return func_y()

@app.route('/sw_g')
def sw_g():
    return func_g()

print(__name__)
if __name__ == '__main__':
    app.run(host='192.168.0.67', port=5000, debug=False)
