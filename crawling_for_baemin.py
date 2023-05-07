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
    
def get_info_for_Baemin(url):
    options = webdriver.ChromeOptions()
    #options.add_argument("headless")

    #url = input()
    #url ="https://www.samsungcareers.com/hr/"

    driver = webdriver.Chrome("chromedriver", options=options)
    driver.get(url)

    time.sleep(10)
    all = driver.find_element(By.CSS_SELECTOR,"#PCAppMain > div.content > section > div > div > div.recruit-list > ul")
    select = all.find_elements(By.TAG_NAME, "li")
    job_list = []

    for elm in select:
        try:
             print("$ ", elm.find_element(By.CSS_SELECTOR,"a > p").get_attribute("textContent"))
            #job_title = get_info(elm, "a")
            #print(job_title)
            # job_period = get_info(elm, "a>span")
            # job_list.append([job_title, job_period])   #TODO 나중에 dictionary로 바꾸기
        except Exception as e:
            # print(e)
            pass
    return job_list
   

print(get_info_for_Baemin("https://career.woowahan.com/?jobCodes=&employmentTypeCodes=&serviceSectionCodes=&careerPeriod=&keyword=&category=jobGroupCodes%3ABA005001#recruit-list"))


    













    
#get_info("#list > li:nth-child(2) > div > div:nth-child(1) > a > h3")

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.select_one("div>a>h3").text)




    