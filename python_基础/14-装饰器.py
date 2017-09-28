def verify(func):
	num = int(input('输入密码：'))
	if num==123456:
		def inner():
			func()
		return inner

	else:
		def inner():
			print('密码错误，不能进行下一步。')
		return inner

@verify
def test():
	num1 = int(input('输入数字1：'))
	num2 = int(input('输入数字2：'))

	print('相加结果为---%d---'%(num1+num2))


test()
