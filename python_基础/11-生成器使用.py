def task1():
#	t2 = task2()
	for i in range(7):
#		next(t2)
		yield i
		print('-------task1------')

def task2():
	t1 = task1()
	for i in range(7):
		next(t1)
		yield i
		print('-------task2------')


t2 = task2()
next(t2)
next(t2)
next(t2)
next(t2)
next(t2)
next(t2)
next(t2)
