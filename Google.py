from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import math
import re

# Стартовая страница
page = "https://2gis.ru/blagoveshensk?queryState=center%2F127.520714%2C50.291313%2Fzoom%2F11"

# Инициализация селениума
driver = webdriver.Chrome()
driver.get(page)
driver.set_page_load_timeout(3)
try:
    search = driver.find_element_by_name('search[query]')
except :
:
    print('Проблемы с определением формы поиска')
print('Определение формы поиска произведено успешно')
driver.set_page_load_timeout(5)
# time.sleep(5)
search_key = 'магазин'
print('Поисковый запрос: "', search_key, '"')
page = search.send_keys(search_key, Keys.ENTER)
driver.set_page_load_timeout(5)
time.sleep(5)

# ПОИСК КОЛИЧЕСТВА СТРАНИЦ
total_count_firms = driver.find_element_by_class_name('searchResults__headerName')
total_count_res_text = total_count_firms.text
digit_total_count_res = re.findall('\d+', total_count_res_text)
print('Количество найденых организаций:',digit_total_count_res )

# НАХОЖДЕНИЕ КОЛИЧЕСТВА СТРАНИЦ

pr_count_iter = int(digit_total_count_res[-1])/12
bb =  math.ceil(pr_count_iter)
print('Количество страниц в справочнике организаций ',bb)
i=1


firm_name = driver.find_elements_by_class_name('miniCard__headerTitle')
print('Найдено' + str(len(firm_name)) + ' элементов на странице:')
index_data = 0
for i in firm_name:
    index_data += 1
    print(' ***', ' ', index_data, ' ', i.text)
    i.click()
    time.sleep(5)

    try:
        phone_number_open = driver.find_element_by_class_name('contact__phonesFadeShow')
        cootacts = phone_number_open.click()
        time.sleep(5)
        phone_num = driver.find_elements_by_class_name('contact__phonesItemLinkNumber')
        for phone in phone_num:
            print(phone.text)
    except selenium.common.exceptions.NoSuchElementException:
        print('Телефон не найден')
        time.sleep(5)
    # поиск номера телефона
    time.sleep(5)


# ОБХОД СТРАНИЦ
# for number in range(2,bb+1):
#     result_page = driver.find_element_by_link_text(str(number))
#     print('вывод результатов поиска селениума', result_page.text)
#     result_page.click()
#
#     time.sleep(5)





