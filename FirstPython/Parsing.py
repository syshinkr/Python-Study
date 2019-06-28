import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈

response = requests.get('http://radibrary.tistory.com')
soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.find('div', {'class' : 'list_content'})
data = []
for item in titles.find_all('a'):
    href = item.herf
    data.append(href)