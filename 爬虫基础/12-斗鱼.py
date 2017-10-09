from selenium import webdriver
from lxml import etree
import urllib.request
import os

def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"}

    driver = webdriver.PhantomJS()
    driver.get("https://www.douyu.com/directory/game/yz")

    page = 1
    while True:
        html = driver.page_source.encode('utf-8')
        xml = etree.HTML(html)
        names = xml.xpath('//span[@class="dy-name ellipsis fl"]')
        # 名字
        name_list = []
        for name in names:
            name_list.append(name.text)

        numbers = xml.xpath('//span[@class="dy-num fr"]')
        # 观众数
        number_list = []
        for number in numbers:
            number_list.append(number.text)

        # 封面
        img_list = xml.xpath('//span[@class="imgbox"]/img/@data-original')

        for index in range(len(img_list)):
            filename = name_list[index] + ' ' + number_list[index] + '.jpg'
            fullname = os.path.join('pics', filename)
            request = urllib.request.Request(url=img_list[index], headers=headers)
            response = urllib.request.urlopen(request).read()

            with open(fullname, 'wb') as f:
                f.write(response)

        print('第%d页下载完成'%page)

        if len(xml.xpath('//a[@class="shark-pager-next shark-pager-disable shark-pager-disable-next"]')) == 0:
            driver.find_element_by_class_name('shark-pager-next').click()
            page += 1

        else:
            print('所有页面下载完成')
            break

    print('浏览器退出！')
    driver.quit()


if __name__ == '__main__':
    main()