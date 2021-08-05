import requests

url = 'https://www.baidu.com'

proxies = {
    'https': 'https://36.248.129.42:9999'
}

resp = requests.get(url, proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
resp.close()
