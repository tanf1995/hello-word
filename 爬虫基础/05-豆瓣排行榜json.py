import urllib.parse
import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action='
ua_header = {
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.8"

}

formdata = {
    "start" : "0",
    "limit" : "40"
}
data = urllib.parse.urlencode(formdata).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=ua_header)
print(urllib.request.urlopen(request).read().decode('utf-8'))



