count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if ((i != j) and (i != k) and (j != k)):
                print(i * 100 + j * 10 + k)
                count += 1
print("总共有%d个" % count)
