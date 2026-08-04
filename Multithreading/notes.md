# Multi Threading
- Multi threading means running multiple threads inside the same program so that the multiple tasks can make progress during the same period.

## Thread
- Thread means a single part of a execution of the program.

***Example***
```py
import threading
def cooking():
    for i in range(10):
        print('Cooking Maggi')

def washing():
    for i in range(10):
        print('Washing cloth')

def cleaning():
    for i in range(10):
        print('Cleaning house')

t1=threading.Thread(target=cooking)
t2=threading.Thread(target=washing)
t3=threading.Thread(target=cleaning)

t1.start()
t2.start()
t3.start()
```