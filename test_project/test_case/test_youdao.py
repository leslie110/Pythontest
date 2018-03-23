# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest,time

class TestYoudao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "http://www.youdao.com"
        self.driver.implicitly_wait(30)

    def test_youdao(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_xpath('''//*[@id="translateContent"]''').clear()
        driver.find_element_by_xpath('''//*[@id="translateContent"]''').send_keys("webdriver")
        driver.find_element_by_xpath('''//*[@id="form"]/button''').click()
        #title = driver.title
        #self.assertEqual(title,u"webdriver")

    def tearDown(self):
        self.driver.quit()

if __name__ =="__main__":
    unittest.main()
