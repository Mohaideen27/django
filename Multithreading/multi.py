import threading
def func1():
    for i in range(100):
        print(i)
def func2():
    for j in range(101,200):
        print(j)
        
def func3():
    for k in range(201,300):
        print(k)

t1=threading.Thread(target=func1)
t2=threading.Thread(target=func2)
t3=threading.Thread(target=func3)


t1.start()
t2.start()
t3.start()