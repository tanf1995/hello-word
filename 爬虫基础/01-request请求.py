import urllib.request

url = "http://www.baidu.com"

ua_header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
}

request = urllib.request.Request(url=url, headers=ua_header)

response = urllib.request.urlopen(request)

html = response.read()

try:
    file = open('测试保存静态页面.html', 'wb')
    file.write(html)
    file.close()
except Exception:
    print('保存失败')
else:
    print('保存成功!')
