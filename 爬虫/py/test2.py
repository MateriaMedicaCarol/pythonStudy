list = []
s = 'soajgosjgoajsogajsogjas'
list.append(s)
print(list)

import csv

f = open('../csv/test.csv', mode='w', encoding='utf-8')
csvwriter = csv.writer(f)

list2 = [
    'magnet:?xt=urn:btih:3076a3e03a412fe7411b8c163030a3dc5f9baad4&dn=[电影天堂www.dytt89.com]老友记重聚特辑-2021_BD中英双字.mp4&tr=http://t.t789.me:2710/announce&tr=http://t.t789.co:2710/announce&tr=http://t.t789.vip:2710/announce']
list3 = ['sjfosj', 'sojog']

# writerow()方法是一行一行写入，writerows方法是一次写入多行。
csvwriter.writerows([list3])

# join 函数  列表中不能有数字
# list4=['avc','gjoa',1]
list4 = ['avc', 'gjoa']
title = 'saas'.join(list4)
print(title)
list5 = [1, 2, 3]
for i in list5:
    print(i, end='')
