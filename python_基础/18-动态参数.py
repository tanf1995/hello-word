def add(*args, **kw):
	sum = 0
	for i in args:
		sum += i
	print(sum)

	for i in kw.keys():
		print(kw[i])

	print(args)
	print(kw)


add(1, 2, 3, text='hello', text2='word')
