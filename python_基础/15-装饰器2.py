def verify(text):
	print(text)
	def inner1(func):	
		num = int(input('输入密码：'))
		if num==123456:
			def inner2():
				func()
			return inner2

		else:
			def inner2():
				print('密码错误，不能进行下一步。')
			return inner2
	return inner1

@verify('hello, 密码为123465')
def test():
	num1 = int(input('输入数字1：'))
	num2 = int(input('输入数字2：'))

	print('相加结果为---%d---'%(num1+num2))

test()
