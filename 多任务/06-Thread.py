from threading import Thread
import threading
import time

def task1():
	for i in range(5):
		print('----task1----')
		time.sleep(1)

def task2():
	for i in range(5):
		print('----task2----')
		time.sleep(1)

t1 = Thread(target=task1)
t2 = Thread(target=task2)

t1.start()
t2.start()

while True:
	leng = len(threading.enumerate())
	print('当前线程数：%d'%leng)
	if leng <= 1:
		break
	time.sleep(1)
