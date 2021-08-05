import re
import requests

url = 'https://www.bilibili.com/video/BV1i54y1h75W'
resp = requests.get(url)
s=resp.text
list=re.findall(r'[\u4e00-\u9fa5]',s)
ls3 = ''.join(list)


with open('../html/bilibili.html', mode='w', encoding='utf-8') as f:
    f.write(ls3)

resp.close()
f.close()
print('over')
