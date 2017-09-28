def test(num):
	print('闭包外层----,传入参数%d'%num)

	def inner(num_in):
		print('闭包内层----,传入参数%d'%num_in)
		print('闭包内层----,内外参数和为%d'%(num_in+num))

	return inner

t = test(100)
t(200)
		


