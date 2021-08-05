from selenium.webdriver import Chrome

web = Chrome()
web.get('https://www.bilibili.com/')
print(web.title)
