# coding: utf-8

# GPIO 라이브러리 호출
import RPi.GPIO as GPIO

# time 모듈
import time

# 핀 번호로 제어 : 핀 번호 할당 -> 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀 번호 : channel 번호
LED = 11

# 11번 채널(핀번호)을 출력 핀으로 등록, 초기 출력은 로우레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# 하이레벨 출력
#GPIO.output(LED, GPIO.HIGH)
# 로우레벨 출력
#GPIO.output(LED, GPIO.LOW)

try:

    while 1:
        
        #하이레벨 출력
        GPIO.output(LED, GPIO.HIGH)

        # 0.5초 대기
        time.sleep(0.5)

        # 로우레벨 출력
        GPIO.output(LED, GPIO.LOW)

        # 0.5초 대기
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

# GPIO 개방
GPIO.cleanup()