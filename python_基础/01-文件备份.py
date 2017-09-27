oldFileName = input('输入你想复制的文件名：')
oldFile = open(oldFileName, 'r')

if oldFile:
	fileFlagNum = oldFileName.find('.')
	if fileFlagNum > 0:
		fileFlag = oldFileName[fileFlagNum:]
	else:
		fileFlag = ''

	newFileName = oldFileName[:fileFlagNum] + '（附件）' + fileFlag

	newFile = open(newFileName, 'w')
	for line in oldFile.readlines():
		newFile.write(line)

	newFile.close()
	oldFile.close()
