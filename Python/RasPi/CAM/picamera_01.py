# coding: utf-8

import picamera
import time
import datetime

# picamera 객체 오브젝트 생성
with picamera.PiCamera() as camera:
    
    # 해상도 설정
    #camera.resolution = (320, 240)

    # 해상도 상태
    res = input('Resolution(1: 320x240, 2: 640x480, 3: 1024X768) >> ')
    if res == '1':
        camera.resolution = (320, 240)
    elif res == '2':
        camera.resolution = (640, 480)
    else :
        camera.resolution = (1024, 768)

    file_name = input('파일 이름을 입력해주세요 >> ')

    camera.start_preview()
    time.sleep(3)
    camera.stop_preview()

    # 촬영 -> 저장
    camera.capture(file_name + '.jpg')