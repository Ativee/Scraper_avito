from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import math
import re

page = "https://2gis.ru/blagoveshensk?queryState=center%2F127.520714%2C50.291313%2Fzoom%2F11"
driver = webdriver.Chrome()
driver.get(page)
driver.set_page_load_timeout(3)
print('провожу поиск формы поиска')
search = driver.find_element_by_name('search[query]')

driver.set_page_load_timeout(5)
time.sleep(5)
page = search.send_keys('магазин',Keys.ENTER)
driver.set_page_load_timeout(5)
time.sleep(5)
# ПОИСК КОЛИЧЕСТВА СТРАНИЦ
# count_pages = driver.find_element_by_class_name('pagination__arrow _right')
# count_pages.click()
# time.sleep(5)
#
# print('Количество страниц ',len())
#
# # ПОИСК ПО ТЕКСТУ ССЫЛКИ
# i =2
# while i < 6:
#     i+=1
#     result_page= driver.find_element_by_link_text(str(i))
#
#     result_page.click()
#     time.sleep(7)



# *** ПОИСК ПО ИМЕНИ КЛАССА
# ПОИСК ОБЩЕГО КОЛИЧЕСТВА ОРГАНИЗАЦИЙ
total_count_res = driver.find_element_by_class_name('searchResults__headerName')
total_count_res_text = total_count_res.text
digit_total_count_res = re.findall('\d+', total_count_res_text)
print('Количество найденых организаций:',digit_total_count_res )

# НАХОЖДЕНИЕ КОЛИЧЕСТВА СТРАНИЦ

pr_count_iter = int(digit_total_count_res[-1])/12

print (pr_count_iter)
# result_pages = driver.find_element_by_link_text()

bb =  math.ceil(pr_count_iter)
print('Количество страниц в поисковой выдаче ',bb)
i=1


firm_name = driver.find_elements_by_class_name('miniCard__headerTitle')
print('Найдено' + str(len(firm_name)) + ' элементов:')
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



    # index_page= str(i)
    # print(index_page)
    # result_page.click()
    #
    # firm_name = driver.find_elements_by_class_name('miniCard__headerTitle')
    # print('Найдено' + str(len(firm_name)) + ' элементов:')
    # index_data = 0
    # for i in firm_name:
    #     index_data += 1
    #     print(' ***', ' ', index_data, ' ', i.text)
    #     i.click()
    #     time.sleep(3)



#
# count_iter = len(result_pages)
# fff = driver.find_element_by_class_name('pagination__page _current')
# print('Текущая страница', fff.text)
#
# for result_page in result_pages:
#
#     print('Вывод результатов с страницы №', result_page.text)
#     time.sleep(3)
#     firm_name = driver.find_elements_by_class_name('miniCard__headerTitle')
#     print('Найдено' + str(len(firm_name)) + ' элементов:')
#     index_data = 0
#     for i in firm_name:
#         index_data += 1
#         print(' ***', ' ', index_data, ' ', i.text)
#         i.click()
#         time.sleep(3)
#
#
#     page_index = int(result_page.text)+1
#     print('Произвожу переход на', page_index,'страницу посковой выдачи')
#     count_pages = driver.find_element_by_class_name('pagination__arrow _right')
#     count_pages.click()
#     # result_page.click()
#     time.sleep(3)
# #
# i.click()
# time.sleep(3)

# # print('Произвожу переход на следующую страницу:')
# i =0
# while i <5:
#     i+=1
#     elm_iters = driver.find_element_by_id('pnnext')
#     elm_iters.click()
#     time.sleep(5)



# elm_iter = driver.find_elements_by_id()_by_id('pnnext')

# for i in elm_iters:
#     i.click()
#     time.sleep(5)

# elm_iter.click()
driver.set_page_load_timeout(5)
time.sleep(5)



