from threading import Thread, Lock
import time

def task1():
	global num
	for i in range(1000000):
		mutex.acquire()
		num += 1
		if mutex:
			mutex.release()
	print('----task1-执行完毕---')
	print(num)

def task2():
	global num
	for i in range(1000000):
		mutex.acquire()
		num += 1
		if mutex:
			mutex.release()
	print('----task2-执行完毕---')
	print(num)


mutex = Lock()
num = 0
t1 = Thread(target=task1)
t2 = Thread(target=task2)

t1.start()
t2.start()

#print('多线程执行完毕！')
#time.sleep(15)
#print(num)
