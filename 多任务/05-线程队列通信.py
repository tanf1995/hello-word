from multiprocessing import Process, Queue
import time

def write(q, i):
	for j in range(5):
		q.put(i)
		print('----%d----'%i)
		time.sleep(1)

q = Queue()

t1 = Process(target=write, args=(q, 1,))
t2 = Process(target=write, args=(q, 2,))
t3 = Process(target=write, args=(q, 3,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print('进程执行结束---')
for i in range(q.qsize()):
	print(q.get())
