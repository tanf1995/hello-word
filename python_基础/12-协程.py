import time

def A():
	while True:
		yield
		print('------A-----')
		time.sleep(0.5)

def B(a):
	while True:
		next(a)
		print('------B-------')
		time.sleep(0.5)

a = A()
B(a)
	
