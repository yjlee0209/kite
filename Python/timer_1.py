import threading
import datetime

count = 0

# call back function
def func_a():
    print('Timer expired')
    print('End time :', datetime.datetime.now())

    global count

    if count == 10:
        return

    count += 1

    threading.Timer(1, func_a).start()


print('Start time :', datetime.datetime.now())

# 10초 후에 함수 실행
threading.Timer(1, func_a).start()