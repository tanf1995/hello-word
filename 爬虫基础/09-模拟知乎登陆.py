import requests
import urllib.parse
from bs4 import BeautifulSoup

def zhihuSignin():
    url = "https://www.zhihu.com/#signin"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }

    sess = requests.session()
    html = sess.get(url=url, headers=headers).text
    bs = BeautifulSoup(html, 'lxml')
    _xrsf = bs.find("input", attrs={"name": "_xsrf"}).get("value")

    data = {
    "_xsrf": _xrsf,
    "password": "tf951021",
    "captcha_type": "cn",
    "email": "18279182695"
    }
    # data = urllib.parse.urlencode(data)
    response = sess.post(url="https://www.zhihu.com/login/email", data=data, headers=headers).content
    print(response.decode('utf-8'))

if __name__=='__main__':
    zhihuSignin()