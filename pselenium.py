from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import  requests
from bs4 import BeautifulSoup
import urllib

page = "https://2gis.ru/moscow/rubrics"
def sel_scrapy(page):
    driver = webdriver.Chrome()
    driver.get(page)
    # driver.set_page_load_timeout(6)
    # time.sleep(5)
    # driver.find_element_by_link_text('Все рубрики').click()
    # driver.get_screenshot_as_file('page_code')
    # rubr
    # time.sleep(5)
    driver.set_page_load_timeout(8)
    rubricks = driver.find_elements_by_class_name('rubricsList__listItemLink')

    for i in rubricks:
        z = i.click()
        time.sleep(3)
        subrubricks = i.find_elements_by_class_name('rubricsList__listItemLink')
        print('Список рубрик: ', i.text)

        for subrubrick in subrubricks:
            lll = subrubrick.find_elements_by_class_name('rubricsList__listItemLink')
            for i in lll:
                i.click()



            print(i.text)
            time.sleep(3)

        print(len(subrubricks))
        # print('***********************************')
        time.sleep(5)

        driver.back()






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
