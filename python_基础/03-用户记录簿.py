print('1.查看当前存在用户')
print('2.增加用户')
print('3.删除用户')
print('4.退出')
print('输入数字进行操作')


while True:
	try:
		num = int(input())
	except Exception:
		continue

	
	
	if num==1:
		f = open('03-记录簿.txt', 'r')
		for line in f.readlines():
			print(line)
		f.close()

	elif num==2:
		f = open('03-记录簿.txt', 'r')
		index = len(f.readlines())+1
		f.close()
		uname = input('用户名：')
		upwd = input('用户密码：')
		f = open('03-记录簿.txt', 'a+')
		f.write('\n' + str(index) + '.' + '用户名：' + uname + '密码：' + upwd)
		f.close()

	elif num==3:
		f = open('03-记录簿.txt', 'r')
		lines = f.readlines()
		f.close()
		
		del_num = int(input('输入用户序号：'))
		f = open('03-记录簿.txt', 'w+')
		print(lines)
		lines[del_num] = ' '
		for line in lines:
			f.write(line)
		f.close()

	else:
		break
	
print('byebye')


		
		
