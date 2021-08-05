# # i = 2
# # print(i ** 3)
#
# def foo(a=None):
#     if a is None:
#         a = []
#     return a
#
#
# b = foo()
# b.append(1)
# c = foo()
# c.append(2)
# print(c)
#
#
def foo2(a=None):
    if a is None:
        a = []
    return a


d = foo2()
d.append(1)
print(d)
e = foo2()
e.append(2)
print(foo2())


def foo(a=[]):
    return a


b = foo()
b.append(1)
c = foo()
c.append(2)
print(foo())


def add(a, b, *args):
    result = a + b
    for arg in args:
        result += arg
    return result


num = (1, 2, 3, 4)
# print(add(1, 2, 3, 4))

re = add(*num)
# a,b 1,2
print(re)
