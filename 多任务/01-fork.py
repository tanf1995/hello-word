import os
import time

pid = os.fork()

num = 0
for i in range(5):
	if pid==0:
		print('----task1----ppid=%s---'%os.getppid())
		time.sleep(0.5)

	else:
		print('----task2----pid=%s---'%pid)
		time.sleep(0.5)

	num += 1
	

print('---num==%d---'%num)
time.sleep(1)
