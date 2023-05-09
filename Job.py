from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"""
사람인의 채용공고를 검색하는 사이트를 오픈하는 코드
"""
def OpenSite():
    options = webdriver.ChromeOptions()
    #options.add_argument("headless")
    driver = webdriver.Chrome()
    url = "https://www.saramin.co.kr/zf_user/search?search_area=main&searchType=default_mysearch"
    driver.get(url)
    time.sleep(5)
    return driver

"""
키워드를 입력받아서 검색을 하는 코드
"""
def SearchJob(keyword):
    driver = OpenSite()
    search = driver.find_element(By.CSS_SELECTOR, "#total_ipt_keyword")






if __name__ == '__main__':
    OpenSite()