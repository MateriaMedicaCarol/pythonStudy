list = ['1', '3', '5', '8']
for i in list:
    for j in list:
        for k in list:
            if i != j and i != k and j != k:
                print(i + j + k)
