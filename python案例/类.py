class TheFirstDemo:
    # def __init__(self):
    #     print("构造方法")
    pass


Kansan = TheFirstDemo()


class CLanguage:
    # 下面定义了2个类变量
    name = "C语言中文网1111"
    add = "http://c.biancheng.net111"

    def __init__(self, name, add):
        # 下面定义 2 个实例变量
        self.name = name
        self.add = add
        print(name, "网址为：", add)

    #    在构造的时候传递参数 会更改上面的两个类变量

    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)




# 将该CLanguage对象赋给clanguage变量
clanguage = CLanguage("C语言中文网2222", "http://c.biancheng.net22222")

# 输出name和add实例变量的值
print(clanguage.name, clanguage.add)
# 修改实例变量的值
clanguage.name = "Python教程"
clanguage.add = "http://c.biancheng.net/python"
# 调用clanguage的say()方法
clanguage.say("人生苦短，我用Python")
# 再次输出name和add的值
print(clanguage.name, clanguage.add)

# 动态增加实例变量
clanguage.money = 159.9
print(clanguage.money)

# 动态删除实例变量
del clanguage.money


# 动态增加方法
def info(self):
    print("---info函数---", self)


print("\n\n")
clanguage.foo = info


clanguage.foo(clanguage)
print("\n\n")

class Person:
    def __init__(self):
        print("正在执行构造方法")

    # 定义一个study()实例方法
    def study(self):
        print(self, "正在学Python")

    def test(self):
        print(self)

    def who(self):
        print(self)


zhangsan = Person()
zhangsan.study()
zhangsan.test()
lisi = Person()
lisi.study()

# 调用类方法
zhangsan.who()

who = zhangsan.who
who()
