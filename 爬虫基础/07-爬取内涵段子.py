import urllib.request
import re

class Spider(object):
    def __init__(self):
        self.switch = True

    def loadPage(self, page):
        # 下载页面
        if page == 1:
            url = "http://www.neihan8.com/wenzi/index.html"
        else:
            url = "http://www.neihan8.com/wenzi/index_" + str(page) + ".html"

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
            }
        request = urllib.request.Request(url=url, headers=header)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(response.read().decode('utf-8'))
        # 匹配规则__段子标题
        rex_title = '<a\shref=".*?"\sclass="title"\stitle=".*?">(.*?)</a>'
        pattern1 = re.compile(rex_title, re.S)
        title_list = pattern1.findall(html)
        # 匹配规则__段子内容
        rex_content = '<div\sclass="desc">(.*?)</div>'
        pattern2 = re.compile(rex_content, re.S)
        context_list = pattern2.findall(html)

        self.write_save(title_list, context_list, page)


    def write_save(self, title_list, context_list, page):
        filename = '内涵段子' + str(page) + '.txt'
        with open(filename, 'w') as f:
            for i in range(len(title_list)):
                f.write('标题：' + title_list[i]+ '\n')
                f.write('内容：' + context_list[i+1]+ '\n\n')

    def control(self):
        # 控制是否继续爬取
        page = int(input('爬去页数->'))
        while True:
            try:
                self.loadPage(page)
            except Exception:
                print('下载段子失败！')
                break
            else:
                print('下载段子成功，当前第%d页'%page)
                choice = input('下载下一页输入n,停止下载输入q->')
                if choice == 'n':
                    page += 1
                else:
                    break


if __name__ == "__main__":
    s = Spider()
    s.control()