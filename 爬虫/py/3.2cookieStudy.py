import requests

url = 'https://passport.17k.com/ck/user/login'
session = requests.session()

data = {
    "loginName": "18577325580",
    "password": "wasd123456"
}
session.post(url, data=data)
# print(resp.text)

url2='https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
resp=session.get(url2)
print(resp.json())


resp.close()