import requests

resp = requests.get(
    'http://tbm-auth.alicdn.com/e99361edd833010b/S3WzwXzbmFTf2odPDTC/1EcqXFH3lwqo45AadBM_296668840147_hd_hq.mp4?auth_key=1627910898-0-0-af5415ec17e8848c01a40571f98333c1')
with open('../videos/玩具枪视频.mp4', mode='wb') as f:
    f.write(resp.content)
    print('下载完成')
f.close()
resp.close()
