from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import  UserAgent
import time

def OpenSite():
    options = Options()
    url = "https://www.saramin.co.kr/zf_user/"
    userAgent = UserAgent()
    options.add_argument(f"user-agent = {userAgent.random}")
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    job_input = driver.find_element(By.XPATH, "//*[@id=\"btn_search\"]")
    job_input.click()
    time.sleep(2)
    keyword_Sender = driver.find_element(By.XPATH, "//*[@id=\"ipt_keyword_recruit\"]")
    keyword_Sender.send_keys('개발자')
    time.sleep(2)
    keyword_search = driver.find_element(By.XPATH, "//*[@id=\"btn_search_recruit\"]")
    keyword_search.click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id=\"content\"]/ul[1]/li[2]/a").click()
    time.sleep(5)
    return driver


def SearchJob(keyword):
    driver = OpenSite()
    driver.find_element(By.XPATH, "//*[@id=\"btn_search\"]").click()





if __name__ == '__main__':
    OpenSite()