# -*- coding: UTF-8 -*-
import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


#访问51job并进入搜索页面
def open51job(url,keys):
    driver = webdriver.PhantomJS(executable_path='/usr/local/phantomjs/bin/phantomjs')
    driver.get(url)
    print u"进入...." + driver.title
    #进入页面，默认搜索框为textbox1
    elem = driver.find_element_by_class_name("textbox1")
    elem.clear()
    elem.send_keys(keys)
    elem.submit()
    #close browser tab
    driver.close()
    #switch to next tab
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    print u"进入...." + driver.title
    time.sleep(2)
    return driver
#搜索工作
def searchJob(driver):
    #获取当前页所有的工作信息
    data = driver.page_source
    content = BeautifulSoup(data, 'lxml')
    position = content.find_all("p", {"class":"t1"})
    company = content.find_all("span", {"class":"t2"})
    location = content.find_all("span", {"class":"t3"})
    salary = content.find_all("span", {"class":"t4"})
    publish = content.find_all("span", {"class":"t5"})
    i = 1
    for each in position:
        print "##################第" + str(i) + "个job###############"
        print u"职位名:" + each.a.get("title")
        print u"职位链接:" + each.a.get("href")
        print u"公司名:" + company[i].string
        print u"工作地点:" + location[i].string
        if salary[i].string == "":
            print u"薪资:" + salary[i].string
        print u"发布时间:" + publish[i].string
        print "\n"
        i = i + 1
    return driver
#切换到下一页
def nextPage(driver):
    try:
        page_num = driver.find_element_by_link_text("下一页")
        page_num.click()
    except NoSuchElementException:
        print u"搜索完毕"
        flag = 0
        return flag

if __name__ == '__main__':
    url = "http://www.51job.com/beijing"
    keys = raw_input("请输入搜索关键词:").decode(sys.stdin.encoding)
    print "请稍等片刻...."
    num = 1
    driver = open51job(url,keys)
    while True:
        print u"#######################第" + str(num) + u"页工作信息如下########################\n"
        driver = searchJob(driver)
        flag = nextPage(driver)
        if flag == 0:
            break
        num = num + 1
    driver.close()