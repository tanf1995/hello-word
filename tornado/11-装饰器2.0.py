#coding=utf-8
import threading
import time

def long_io():
	num = 0
	print('------处理中-----')
	for i in range(5):
		print('-----%d-----'%i)
		num += 1
		time.sleep(1)
	print('------处理结束-----')
	yield num

def gen_con(func):
	def inner():
		gen = func() 
		f = next(gen)
		def inner2(f):
			ret = next(f)
			try:
				gen.send(ret)
			except StopIteration:
				pass
		t1 = threading.Thread(target=inner2, args=(f, ))
		t1.start()
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
