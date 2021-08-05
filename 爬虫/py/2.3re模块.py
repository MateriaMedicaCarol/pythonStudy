import re

# r  原始字符串 raw strings

# findall  匹配字符串中所有符合正则的内容
list = re.findall(r'\d+', '19989,32932,nihao32099,fei29812389')
print(list)

# finditer  返回一个迭代器
it = re.finditer(r'\d+', '19989,32932,nihao32099,fei29812389')
print(it)
for i in it:
    print(i)
print('----------------')

# 迭代器只能向前而不能后退 所以需要再创建一次
it = re.finditer(r'\d+', '19989,32932,nihao32099,fei29812389')
for i in it:
    print(i.group())

print('\n')
print('search')
s = re.search(r'\d+', '19989,32932,nihao32099,fei29812389')
# search返回一个match对象,找到一个结果就返回
print(s)
print(s.group())
print(s.span())

# 从头开始匹配 相当于'^\d+'
# m=re.match(r'\d+', 'sd9989,32932,nihao32099,fei29812389')
# print(m.group())

# 预加载正则表达式  可以让代码效率提高一点
print('\n')
print('预加载正则表达式')
obj = re.compile(r'\d+')
ret = obj.findall('sd9989,32932,nihao32099,fei29812389\'')
print(ret)
ret1 = obj.finditer('sd9989,32932,nihao32099,fei29812389')
for i in ret1:
    print(i.group())

s = """
   <div class='jisnog'><span title="1" ></span></div> 
   <div class='sdfas'><span title="2" ></span></div> 
   <div class='adsf'><span title="3" ></span></div> 
   <div class='sagsg'><span title="4" ></span></div> 
   <div class='sdghs'><span title="5" ></span></div> 
"""
obj=re.compile(r"""<div class='(?P<class>.*?)'><span title="(?P<title>\d)" ></span></div>""",re.S)
# re.S 使 . 也可以匹配换行符
s=obj.finditer(s)
for i in s:
    print(i.group("class"))
