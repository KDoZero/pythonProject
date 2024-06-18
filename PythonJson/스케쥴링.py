import schedule
import time     # 일정 시간만큼 대기를 걸기 위해
import requests # 서버와 http 동기 통신을 하기 위해서
from bs4 import BeautifulSoup

def perform_web_crawling():
    url = "http://www.naver.com"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("웹 크롤링을 수행합니다.")
    perform_web_crawling()

# schedule.every().day.at("09:44").do(job)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()  # 대기 중인 작업을 수행하는 함수
    time.sleep(1)   # 1초 대기