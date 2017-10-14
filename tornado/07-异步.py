#coding=utf-8
import threading
import time


def long_io():
	def func():
		print('------处理中-----')
		for i in range(5):
			print('-----%d-----'%i)
			time.sleep(1)
		print('------处理结束-----')
	t1 = threading.Thread(target=func)
	t1.start()

def a():
	print('------a-----开始-')
	long_io()
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
