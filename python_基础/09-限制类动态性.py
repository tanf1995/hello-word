import types

class Test():
	__slots__ = ('name', 'age', 'run')

	def __init__(self, name, age):
		self.name = name
		self.age = age


a = Test('tf', 20)

print(a.name)
print(a.age)

try:
	a.gender = 'male'
	print(a.gender)
except Exception:
	print('动态添加属性出错')

def run(self):
	print('----run方法----')

try:
	a.run = types.MethodType(run, a)
	a.run()
except Exception:
	print('动态添加类方法出错')
