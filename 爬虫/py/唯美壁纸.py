import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.umei.net/bizhitupian/weimeibizhi/'
resp = requests.get(url)
resp.encoding = 'utf-8'

main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find('div', class_='TypeList').find_all('a')
for a in alist:
    img_url = 'https://www.umei.net' + a.get('href')  # 直接通过get就可以拿到属性的值
    child_page_resp = requests.get(img_url)
    child_page_resp.encoding = 'utf-8'
    child_page = BeautifulSoup(child_page_resp.text, 'html.parser')
    p = child_page.find('p', align='center')
    img = p.find('img')
    # print(img)
    # beautifulsoup 中通过get来拿标签中属性的值
    src = img.get('src')

    # 下载图片
    img_resp = requests.get(src)
    img_name = src.split('/')[-1]
    with open('img/' + img_name, mode='wb') as f:
        f.write(img_resp.content)
    print('over!!!', img_name)
    time.sleep(1)
resp.close()

