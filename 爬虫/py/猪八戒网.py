# xpath 练习
from lxml import etree
import requests

url = 'https://guilin.zbj.com/search/f/?type=new&kw=saas'
resp = requests.get(url)
result = etree.HTML(resp.text)
divs = result.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for div in divs:
    price = div.xpath('./div/div/a/div[2]/div[1]/span[1]/text()')[0].strip('¥')
    title_=div.xpath('./div/div/a/div[2]/div[2]/p/text()')
    title='saas'.join(div.xpath('./div/div/a/div[2]/div[2]/p/text()'))

    # title=title_[0]+'saas'+title_[1]
    # print(price)
    print(title)
    break



resp.close()
