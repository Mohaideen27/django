# Multi Threading

- Multi threading means running multiple threads inside the same program so that the multiple tasks can make progress during the same period.

## Thread

- Thread means a single part of a execution of the program.

**_Example_**

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

# Parsing Technique

- It is a process of providing the security to the data while storing the data or while sending the data from source to destination.

**_for converting data to string use json_**

```py
import json
import json

data=[10,20,30,40]
enc=json.dumps(data)
print(enc,type(enc))
dec=json.loads(enc)
print(dec,type(dec))

```

**_for converting data to bytes use pickle_**

```py
import pickle

data=[10,20,30,40]
enc=pickle.dumps(data)
print(enc,type(enc))
dec=pickle.loads(enc)
print(dec,type(dec))
```
