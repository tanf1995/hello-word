#coding=utf-8
import threading
import time

gen = None

def long_io():
	def func():
		global gen
		num = 0
		print('------处理中-----')
		for i in range(5):
			print('-----%d-----'%i)
			num += 1
			time.sleep(1)
		print('------处理结束-----')
		try:
			gen.send(num)
		except StopIteration:
			pass
	t1 = threading.Thread(target=func)
	t1.start()

def gen_con(func):
	def inner():
		global gen
		gen = func() 
		next(gen)
	return inner

@gen_con
def a():
	print('------a-----开始-')
	ret = yield long_io()
	print("a返回的num为%d"%ret)
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
