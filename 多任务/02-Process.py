from multiprocessing import Process
import time

def task1():
	for i in range(5):
		print('----task1---')
		time.sleep(0.5)

def task2():
	for i in range(5):
		print('----task2---')
		time.sleep(0.5)

def task3():
	for i in range(5):
		print('----task3---')
		time.sleep(0.5)

t1 = Process(target=task1, name='t1')
t2 = Process(target=task2)
t3 = Process(target=task3)

print('多进程开始')
t1.start()
t2.start()
t3.start()

print(t1.name)
print(t2.name)
print(t3.name)

t1.join()
t2.join()
t3.join()

print('多进程结束')
