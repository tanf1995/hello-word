from multiprocessing import Pool
import time

def task(num):
	for i in range(5):
		print('---传入了%d---'%num)
		time.sleep(1)

pool = Pool(5)

for i in range(6):
	pool.apply(task, (i,))

pool.close()
pool.join()
