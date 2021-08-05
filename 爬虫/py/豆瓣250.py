# pandas
import requests
import re
import csv

paixu = 1
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
}
for begin in range(0, 226, 25):
    url = f'https://movie.douban.com/top250?start={begin}'
    resp = requests.get(url, headers=headers)
    obj = re.compile(
        r"""<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?average">(?P<score>.*?)</span>""",
        re.S)
    results = obj.finditer(resp.text)
    f = open('../csv/豆瓣250.csv', mode='a', encoding='utf-8', newline='')
    csvwriter = csv.writer(f)
    for it in results:
        # print(it.group("name"))
        # print(it.group("year").strip())
        # print(it.group("score"))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        dic['xuhao'] = paixu
        paixu += 1
        print(dic)
        csvwriter.writerow(dic.values())

resp.close()
