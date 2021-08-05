import requests

query = input('输入一个你喜欢的歌手')
url = f'https://www.sogou.com/web?query={query}'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
}
resp = requests.get(url, headers=header)
print(resp.text)
