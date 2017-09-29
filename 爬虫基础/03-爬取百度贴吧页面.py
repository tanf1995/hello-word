import os
import urllib.request
import urllib

# loc = os.path.join('04-myhtml', 'h1.txt')
# file = open(loc, 'w')
# file.write('haha')
# file.close()

def tiebaSprider(url, name, bPage, ePage):
    #爬取网页
    ua_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
    }
    for page in range(bPage, ePage+1):
        url = url + '&pn=' + str((page-1)*50)
        request = urllib.request.Request(url=url, headers=ua_header)

        print('---正在下载第%d页---'%page)
        respond = urllib.request.urlopen(request)
        res = respond.read()
        print('----下载成功---')

        print('---正在保存页面---')
        save_file(res, page)
        print('---保存成功---')

def save_file(res, page):
    filename = '第' + str(page) + '页.html'
    file = os.path.join('04-myhtml', filename)
    with open(file, 'wb') as f:
        f.write(res)

if __name__ == '__main__':
    url = "http://tieba.baidu.com/f"

    tiebaName = input('请输入贴吧名：')
    tiebaName = urllib.parse.urlencode({'kw': tiebaName})
    url = url + '?' + tiebaName

    beginPage = int(input('输入起始页：'))
    endPage = int(input('输入结束页：'))
    tiebaSprider(url, tiebaName, beginPage, endPage)
