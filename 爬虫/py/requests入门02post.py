import requests

url = 'https://fanyi.baidu.com/sug'
s = input('请输入要翻译的单词')
data = {
    'kw': s
}
response = requests.post(url, data=data)
print(response.text)
print('-----------')
print(response.json())
