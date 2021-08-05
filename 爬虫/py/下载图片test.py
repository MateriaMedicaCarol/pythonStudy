import requests

src = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_match%2F0%2F11525413502%2F0.jpg&refer=http%3A%2F%2Finews.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628039304&t=14f66b1a707b6de00ccdbdd53e9c6613'
resp = requests.get(src)
print(resp.content)

resp.close()
