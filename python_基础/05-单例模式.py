class Sing_ex(object):
	__has_obj = False
	__the_obj = None

	def __init__(self, name):
		if self.__has_obj == False:
			self.name = name
			self.__has_obj = True

	def __new__(cls, name):
		if not cls.__the_obj:
			cls.__the_obj = object.__new__(cls)
			return cls.__the_obj
		else:
			return cls.__the_obj

s = Sing_ex('tf')
print(s.name)
print(id(s))

s2 = Sing_ex('jj')
print(s2.name)
print(id(s2))
