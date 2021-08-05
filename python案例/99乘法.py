# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d*%d=%d" % (j, i, i * j), end=' ')
#     print()

# motheds 2
for i in range(1, 10):
    for j in range(1, i + 1):
        # print("%d*%d=%d" % (j, i, i * j), end=' ')
        print("{}*{}*{}".format(i, j, j * i), end=' ')
    print()
