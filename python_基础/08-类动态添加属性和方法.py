import types

class Test():
	def __init__(self, name):
		self.name = name

	def run(self):
		print('-----%s奔跑------'%self.name)

def eat(self):
	print('-----%s吃饭中----'%self.name)


p = Test('tf')
print(p.name)
p.run()

print('-----动态添加的属性和类——----')
p.age = 20
p.eat = types.MethodType(eat, p)

print(p.age)
p.eat()
