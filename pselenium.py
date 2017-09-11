from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

page = "https://2gis.ru/"
def sel_scrapy(page):
    driver = webdriver.Chrome()

    driver.get(page)
    time.sleep(5)
    driver.find_element_by_link_text('Все рубрики').click()
    time.sleep(15)
    rubricks = driver.find_element_by_class_name('rubricsList__listItem')
    time.sleep(15)
    print(rubricks)
    time.sleep(15)


sel_scrapy(page)
