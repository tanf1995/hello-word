import urllib.request
import urllib.parse
import http.cookiejar

cookiejar = http.cookiejar.CookieJar()

handler = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(handler)

opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")]

# 人人网的可用登录接口
url = "http://www.renren.com/PLogin.do"
# 个人账号
data = {
    'email': '18279182695',
    'password': 'tf951021'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data)

response = opener.open(request)

print(response.read().decode('utf-8'))



