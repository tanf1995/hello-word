class A(object):
	def test(self):
		print('-----A-----')


class B(object):
	def test(self):
		print('-----B-----')

class C(B, A):
	pass

c = C()
c.test()
