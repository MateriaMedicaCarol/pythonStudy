import re
import requests
import csv

download_list=[]
domain = 'https://www.dytt89.com'
resp = requests.get(domain, verify=False)  # 去掉安全验证
resp.encoding = 'gb2312'
result = resp.text
obj = re.compile(r'2021必看热片.*?<ul>(?P<child_result>.*?)</ul>', re.S)
# obj1 = re.compile(r"<a href='(?P<href>.*?)'>", re.S)
obj1=re.compile(r"""<li><a href='(?P<href>.*?)'""",re.S)
objsub=re.compile(r'.*?style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_addr>.*?)">',re.S)


# 子迭代器
child_result_Iterator  = obj.finditer(result)
for it in child_result_Iterator:
    child_result=it.group('child_result')

    final_result_Iterator = obj1.finditer(child_result)
    for itt in final_result_Iterator:
        final_result=domain+itt.group('href')
        #         子页面
        resp2=requests.get(final_result,verify=False)
        resp2.encoding='gb2312'
        supage=resp2.text
        # print(supage)
        download_addr_interator=objsub.finditer(supage)
        for ittt in download_addr_interator:
            s=ittt.group('download_addr')
            download_list.append(s)





f=open('../csv/电影天堂下载链接.csv', mode='a', encoding='utf-8', newline='')
csvwrite=csv.writer(f)
for i in download_list:
    csvwrite.writerow([i])

resp.close()
