
import csv
import requests
from bs4 import BeautifulSoup

f=open('../csv/蔬果价格.csv', mode='a', encoding='utf-8', newline='')
csvwriter=csv.writer(f)
csvwriter.writerow(['品名','最低价','平均价','最高价','单位'])

for begin in range(1,5):
    url = f'http://www.xinfadi.com.cn/marketanalysis/0/list/{begin}.shtml'
    resp = requests.get(url)

    page = BeautifulSoup(resp.text, 'lxml')  # 创建一个bs4对象，指定HTML解析器
    # table=page.find('table',class_='hq_table')
    table = page.find('table', attrs={'class': 'hq_table'})
    # print(table)
    table1 = table.find_all('tr')[1:]
    for i in table1:
        tds = i.find_all('td')
        name = tds[0].text
        lowest_price = tds[1].text
        avr_price = tds[2].text
        highest_price = tds[3].text
        unit = tds[5].text
        csvwriter.writerow([name, lowest_price, avr_price, highest_price, unit])

f.close()
resp.close()