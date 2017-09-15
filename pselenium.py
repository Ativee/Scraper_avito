from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import  requests
from bs4 import BeautifulSoup
import urllib

page = "https://2gis.ru/moscow/rubrics"
def sel_scrapy(page):
    # Открываю страницу определенного города
    driver = webdriver.Chrome()
    driver.get(page)
    # driver.set_page_load_timeout(6)
    # time.sleep(5)
    # driver.find_element_by_link_text('Все рубрики').click()
    # driver.get_screenshot_as_file('page_code')
    # rubr
    # time.sleep(5)
    driver.set_page_load_timeout(5)
    # Поиск всех рубрик
    rubricks = driver.find_elements_by_class_name('rubricsList__listItemLink')
    print('Всего найдено: ', len(rubricks), ' рубрик')
    # Обход всех рубрик и открытие подрубрик
    for rub in rubricks:

        print(str(rubricks.index(rub)+1) + ' '+ str(rub.text))
        # open_subrubrick = rub.click()
        driver.set_page_load_timeout(3)
       
        # print(art)


        # Поиск всех подрубрик

        subrubricks = rub.find_element_by_xpath('//*[@id="module-1-13-2-1"]/div/section/div[2]/ul/li[2]/h3/a')
        print('Тип subrubricks: ' + str(type(subrubricks)))
        print('************************')
        # print('Найдено '+ str(len(subrubricks))+ ' подрубрик')
        print('Найдена одна подрубрика:')
        # for i in subrubricks:
        #     print(i.text)



        print('***********************************')
        # time.sleep(180)
        driver.back()
        # обход всех подрубрик и поиск всех фирм
        # for subrubrick in subrubricks:
        #     lll = subrubrick.find_elements_by_class_name('rubricsList__listItemLink')
        #     print()
        #     открытие фирм
        #     for i in lll:
        #         i.click()
        #     print(i.text)
        #     time.sleep(3)








        # r = requests.get(page)
        #
        # soup = BeautifulSoup(r.content,'html.parser')
        # sub_sub = soup.find_all('a', class_='link _scheme_none rubricsList__listItemLinkTitle')
        # print(len(sub_sub))
        # sub_sub_list =[]
        # for i in sub_sub[27:]:
        #     sub_sub_list.append(i)
        #
        #     print(i)









sel_scrapy(page)
