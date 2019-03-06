# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup as BS

browser = webdriver.Firefox()
browser.get('http://www.icourse163.org/category/all')
page = browser.page_source
#print(page)
soup = BS(page, 'lxml')
xx = int(soup.find_all(name='a',class_='th-bk-main-gh')[-2].string)
print(xx)
yy = soup.find_all(name='span',class_='u-course-name')
print(yy)
for i in yy:
    zz = i.parent['href']
    print(zz)