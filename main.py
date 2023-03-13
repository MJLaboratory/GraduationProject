import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
'''
html = urllib.request.urlopen("https://sldict.korean.go.kr/front/sign/signContentsView.do?current_pos_index=0&origin_no=23933&searchWay=&top_category=CTE&category=&detailCategory=&searchKeyword=&pageIndex=1&pageJumpIndex=")
soup = BeautifulSoup(html, "html.parser")


print(soup.find_all("a", id = "videoArea")) #수형 이미지
print(soup.find("a", class_ = "example").attrs['href']) #수형 이미지
print(soup.find("dt", class_ = "tooltip2", string = "수형 설명").find_next("dd").get_text()) #수형 설명
print(soup.find("span", string = "한국어 대응표현").parent.find_next("dd").get_text()) #한국어 대응표현
'''

main_url = 'https://sldict.korean.go.kr/front/sign/signList.do?top_category=CTE'
driver = webdriver.Chrome()
driver.get(main_url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#lst = []
for div in soup.find_all("span", class_ = "tit"):
    no = div.find("a")['href'].split("'")[1]
    print(no)
#print(soup.find_all("span", class_ = "tit").find("a")['href'])
#print(soup.find_all("span", class_ = "tit"))

#url = 'https://sldict.korean.go.kr/multimedia/multimedia_files/convert/20200901/739060/MOV000251190_700X466.webm'
#urllib.request.urlretrieve(url, './test.mp4')

driver = webdriver.Chrome()
#driver.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get('https://sldict.korean.go.kr/front/sign/signContentsView.do?current_pos_index=0&origin_no=23933&searchWay=&top_category=CTE&category=&detailCategory=&searchKeyword=&pageIndex=1&pageJumpIndex=')
#time.sleep(3)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
video_link = soup.find("a", id = "videoArea").find("video").find("source")['src']
image_link = soup.find("a", class_ = "example").attrs['href']
descr = soup.find("dt", class_ = "tooltip2", string = "수형 설명").find_next("dd").get_text()
kor_mean = soup.find("span", string = "한국어 대응표현").parent.find_next("dd").get_text()
print(video_link)
print(image_link)
print(descr)
print(kor_mean)

