#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
import unittest
from bs4 import BeautifulSoup as bs

class Douyu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.num = 0
        self.count = 0

    def test_douyu(self):
        self.driver.get("https://www.douyu.com/directory/game/yz")

        while True:
            soup = bs(self.driver.page_source, 'lxml')
            names = soup.find_all('h3', {'class': 'ellipsis'})
            numbers = soup.find_all("span", {"class" :"dy-num fr"})

            for name, number in zip(names, numbers):
                print("观众人数: -" + number.get_text().strip() + "-\t房间名: " + name.get_text().strip())
                # self.num += 1

            # 如果在页面源码里找到"下一页"为隐藏的标签，就退出循环
            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break

            # 一直点击下一页
            self.driver.find_element_by_class_name("shark-pager-next").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()