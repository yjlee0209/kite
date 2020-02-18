import threading
import datetime

def on_timer(count):
    count += 1
    print(count)
   
    timer = threading.Timer(1, on_timer, args=[count])
    timer.start()

    if count == 10:
        print('Canceling Timer...')
        timer.cancel()

print('Starting Timer')
on_timer(0)