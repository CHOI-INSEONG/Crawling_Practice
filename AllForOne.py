from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
"""
지정된 CSS에서 텍스트 가
:css_selector 데이터를 가져올 DOM CSS
"""
def get_info(target, css_selector):
    elm = target.find_element(By.CSS_SELECTOR, css_selector)
   #print(elm.__getattribute__('class'))
    return elm.text
"""

"""
def get_info_attribute(target, css_selector):
    elm = target.find_element(By.CSS_SELECTOR, css_selector).get_attribute("textContent")
    return elm

"""
1. url을 매개변수로 받아서 사이트를 오픈함
"""
def OpenSite(url, css):
    options = webdriver.ChromeOptions()
    #options.add_argument("headless")

    driver = webdriver.Chrome("chromedriver", options=options)
    driver.get(url)
    time.sleep(15) #TODO 페이지가 로드될때까지 기다리는 함수로 변경

    # try:
    #     element = WebDriverWait(driver, 15).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, css))
    #     )

    # finally:
    #     pass

    return driver
        
"""
삼성용
사이트에서 채용공고의 전체 영역을 가져온 뒤, 각각의 공고 항목을 가져오는 함수
"""
def get_info_for_Samsumg(url):
    driver = OpenSite(url,"#list")
    all = driver.find_element(By.CSS_SELECTOR,"#list")
    print(all)
    select = all.find_elements(By.TAG_NAME, "li")
    job_list = []

    for elm in select:
        job_title = get_info(elm, "div > div:nth-child(1) > a > h3" )
        job_period = get_info(elm, "div > div:nth-child(1) > a > p.info > span.period" )
        job_list.append([job_title, job_period])   #TODO 나중에 dictionary로 바꾸기
    return job_list


"""
배민용
사이트에서 채용공고의 전체 영역을 가져온 뒤, 각각의 공고 항목을 가져오는 함수
"""
def get_info_for_Baemin(url):
    driver = OpenSite(url, "#PCAppMain > div.content > section > div > div > div.recruit-list > ul")
    all = driver.find_element(By.CSS_SELECTOR,"#PCAppMain > div.content > section > div > div > div.recruit-list > ul")
    select = all.find_elements(By.TAG_NAME, "li")
    job_list = []

    for elm in select:
        try:
            job_title = get_info_attribute(elm, "a>p")
            # job_period = get_info(elm, "a>span")
            job_list.append([job_title])   #TODO 나중에 dictionary로 바꾸기
        except Exception as e:
            # print(e)
            pass
    return job_list



if __name__ == '__main__':
    # print(get_info_for_Samsumg("https://www.samsungcareers.com/hr/"))
    print(get_info_for_Baemin("https://career.woowahan.com/?jobCodes=&employmentTypeCodes=&serviceSectionCodes=&careerPeriod=&keyword=&category=jobGroupCodes%3ABA005001#recruit-list"))



