from selenium import webdriver
from selenium.webdriver.common.keys import Keys

page = "http://www.google.ru"
driver = webdriver.Chrome()
driver.get(page)
driver.set_page_load_timeout(3)
search = driver.find_element_by_name('q')
search.send_keys('погода')
driver.set_page_load_timeout(5)
search.send_keys(Keys.BACK_SPACE)
driver.set_page_load_timeout(5)

