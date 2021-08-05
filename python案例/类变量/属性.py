# class Clanguage:
#     name = '2123'
#     add = 'asjfo'
#
#     def __init__(self):
#         self.name = 'name'
#         self.add = 'add'
#
#     def say(self):
#         print('say')
#
#     #     类方法
#     @classmethod
#     def info(cls):
#         print("类方法", cls)
#
#
# clanguage = Clanguage()
# print(clanguage.add)
#
# # 通过类对象没有办法修改类变量  这样做相当于给该对象定义新的实例变量
# clanguage.add = 'sdjflsaj'
# print(clanguage.add)
#
# c2 = Clanguage()
# print(c2.add)
#
# Clanguage.add = 'asjfoasdjfoias'
# print(c2.add)
#
# # 实例方法最好通过类对象调用，通过类名调用需要自己给self传递参数
# clang = Clanguage()
# Clanguage.say(clang)
#
# # 类方法最好通过类名调用
# Clanguage.info()
# clang.info()


class People:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        # print('%s 说：我 %d 岁' % (self.name, self.age))
        # print(f'__weight:{self.__weight}')
        # print('end')
        pass



print('-----------------')
p = People('Xiaoping', 12, 100)
print(p.name)
print('------------------')
p.speak()

print('-------------')
