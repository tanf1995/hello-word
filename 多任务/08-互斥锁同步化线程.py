from threading import Thread, Lock
import time

def task1():
	for i in range(10):
		if mutex1.acquire():
			print('-----task----1-')
			mutex2.release()
			time.sleep(1)

def task2():
	for i in range(10):
		if mutex2.acquire():
			print('-----task----2-')
			mutex3.release()
			time.sleep(1)

def task3():
	for i in range(10):
		if mutex3.acquire():
			print('-----task----3-')
			mutex1.release()
			time.sleep(1)

mutex1 = Lock()
mutex2 = Lock()
mutex3 = Lock()
mutex2.acquire()
mutex3.acquire()

t1 = Thread(target=task1)
t2 = Thread(target=task2)
t3 = Thread(target=task3)

t1.start()
t2.start()
t3.start()
