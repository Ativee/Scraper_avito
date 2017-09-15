from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

page = "http://www.google.ru"
driver = webdriver.Chrome()
driver.get(page)
driver.set_page_load_timeout(3)
search = driver.find_element_by_name('q')
driver.set_page_load_timeout(5)
time.sleep(5)
page = search.send_keys('стоматологии москва email',Keys.ENTER)
driver.set_page_load_timeout(5)
time.sleep(5)
nxt = driver.find_elements_by_class_name('g')
print('Найдено'+ str(len(nxt))+' элементов:')
for i in nxt:
    print('******************')
    print(i.text)
print('Произвожу переход на следующую страницу:')
elm_iter = driver.find_element_by_id('pnnext')

elm_iter.click()
driver.set_page_load_timeout(5)
time.sleep(5)



