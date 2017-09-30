import urllib.request
import urllib

keyword = input('翻译关键字->')
formdata = {
    'i': keyword,
    'from':'AUTO',
    'to':'AUTO',
    # 'smartresult':'dict',
    'client':'fanyideskweb',
    # 'salt':'1506699298578',
    # 'sign':'120a9ef95eb967e5625820f8d1ae7599', #反爬虫
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'true',
}

data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom= HTTP/1.1'

header = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}
request = urllib.request.Request(url, data=data, headers=header)

response = urllib.request.urlopen(request)

# print(data)
print(response.read().decode(encoding='UTF8'))


