#coding=utf-8
import threading
import thread
import time


def long_io(cb):
	def func(cb):
		print('------处理中-----')
		num = 0
		for i in range(5):
			print('-----%d-----'%i)
			num += 1
			time.sleep(1)
		print('------处理结束-----')
		cb(num)
#	t1 = threading.Thread(target=func, args=(cb, ))
#	t1.start()
	thread.start_new_thread(func, (cb, ))

def final_show(res):
	print res

def a():
	print('------a-----开始-')
	ret = long_io(final_show)
	print('------a-----结束-')

def b():
	print('------b-----开始-')
	time.sleep(2)
	print('------b-----结束-')


def main():
	a()
	b()
	while 1:
		pass


if __name__ == "__main__":
	main()
