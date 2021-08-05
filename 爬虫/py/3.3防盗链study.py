import requests
import os

# 网页原始链接
# https://www.pearvideo.com/video_1735823


# XHR
# https://www.pearvideo.com/videoStatus.jsp?contId=1735823&mrd=0.7480716278666082

# XHR_video
# https://video.pearvideo.com/mp4/adshort/20210721/1626838118141-15724018_adpkg-ad_hd.mp4


# video url
# https://video.pearvideo.com/mp4/adshort/20210721/cont-1735823-15724018_adpkg-ad_hd.mp4

url = 'https://www.pearvideo.com/video_1735823'
contId = url.split('_')[1]
# print(contId)
videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.7480716278666082'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": f"https://www.pearvideo.com/video_{contId}"
}
resp = requests.get(videoStatusUrl, headers=headers)
dict = resp.json()
videoSrc = dict['videoInfo']['videos']['srcUrl']

systime = dict['systemTime']
videoUrl = videoSrc.replace(systime, f'cont-{contId}')
# print(videoUrl)
# with open("videos/a.mp4", mode='wb') as f:
videoName = 'a.mp4'

with open("videos/" + videoName, mode='wb') as f:
    f.write(requests.get(videoUrl).content)
f.close()

resp.close()
