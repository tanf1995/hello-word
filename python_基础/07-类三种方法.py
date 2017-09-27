class A(object):
	def test(self, x):
		print('实例方法，传入参数%s'%x)

	@classmethod
	def class_test(cls, x):
		print('类方法，传入参数%s'%x)
		
	@staticmethod
	def static_test(x):
		print('静态方法，传入参数%s'%x)

a = A()

a.test(10)
A.class_test(20)
a.test(30)
