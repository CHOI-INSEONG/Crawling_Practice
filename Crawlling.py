from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

"""
지정된 CSS에서 텍스트 가
:css_selector 데이터를 가져올 DOM CSS
"""
def get_info(target, css_selector):
    elm = target.find_element(By.CSS_SELECTOR, css_selector)
   #print(elm.__getattribute__('class'))
    return elm.text
    
def get_info_for_Samsumg(url):
    options = webdriver.ChromeOptions()
    #options.add_argument("headless")

    #url = input()
    #url ="https://www.samsungcareers.com/hr/"

    driver = webdriver.Chrome("chromedriver", options=options)
    driver.get(url)

    time.sleep(3)
    all = driver.find_element(By.CSS_SELECTOR,"#list")
    print(all)
    select = all.find_elements(By.TAG_NAME, "li")
    job_list = []

    for elm in select:
        job_title = get_info(elm, "div > div:nth-child(1) > a > h3" )
        job_period = get_info(elm, "div > div:nth-child(1) > a > p.info > span.period" )
        job_list.append([job_title, job_period])   #TODO 나중에 dictionary로 바꾸기
    return job_list
   

print(get_info_for_Samsumg("https://www.samsungcareers.com/hr/"))


    













    
#get_info("#list > li:nth-child(2) > div > div:nth-child(1) > a > h3")

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.select_one("div>a>h3").text)




    