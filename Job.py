from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"""
������� ä����� �˻��ϴ� ����Ʈ�� �����ϴ� �ڵ�
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
Ű���带 �Է¹޾Ƽ� �˻��� �ϴ� �ڵ�
"""
def SearchJob(keyword):
    driver = OpenSite()
    search = driver.find_element(By.CSS_SELECTOR, "#total_ipt_keyword")






if __name__ == '__main__':
    OpenSite()