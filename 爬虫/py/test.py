# example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(example[:-4])

import os

# os.mkdir('abcabc')

from threading import Thread
# import _thread
import time


def func():
    for i in range(1, 10):
        print('func', i)
        time.sleep(1000000)


def mainfunc():
    for i in range(1, 10):
        print('mainfunc', i)


t1 = Thread(target=func())
t1.start()
t2 = Thread(target=mainfunc())
t2.start()

# coding=utf-8
# import threading
# from time import ctime, sleep
#
#
# def music(func):
#     for i in range(2):
#         print("I was listening to %s. %s" % (func, ctime()))
#         sleep(50)
#
#
# def move(func):
#     for i in range(2):
#         print("I was at the %s! %s" % (func, ctime()))
#         sleep(1)
#
#
# threads = []
# t1 = threading.Thread(target=music, args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move, args=(u'阿凡达',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#
#     print("all over %s" % ctime())
