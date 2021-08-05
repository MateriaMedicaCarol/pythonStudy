# import threading
import requests

urls = [
    f'https://www.cnblogs.com/#{page}'
    for page in range(1, 51)
]


def craw(url):
    resp = requests.get(url)
    print(url, len(resp.text))

