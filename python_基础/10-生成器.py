def generator_test():
	for i in range(5):
		res = yield i
		print(i)
		print(res)

g = generator_test()

next(g)
next(g)
next(g)
g.send('使用sned方法')
next(g)
