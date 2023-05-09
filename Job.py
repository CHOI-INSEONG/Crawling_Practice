from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import  UserAgent
import time
class Crawler:
    def __init__(self):
        options = Options()
        self.url = "https://www.saramin.co.kr/zf_user/"
        userAgent = UserAgent()
        options.add_argument(f"user-agent = {userAgent.random}")
        self.driver = webdriver.Chrome()

    def SearchJob(self, keyword):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id=\"btn_search\"]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id=\"ipt_keyword_recruit\"]").send_keys(keyword)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id=\"btn_search_recruit\"]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id=\"content\"]/ul[1]/li[2]/a").click()
        time.sleep(5)
        job_list = self.driver.find_elements(By.CLASS_NAME, "job_tit")
        for job in job_list:
            print(job.text)



if __name__ == '__main__':
    job_list = Crawler()
    job_list.SearchJob("호텔리어")
