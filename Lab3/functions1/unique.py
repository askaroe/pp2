def unique(my_list):
    d = {}
    l = []
    for i in my_list:
        if(i not in d):
            d[i] = 1
        else:
            d[i] += 1

    for x, y in d.items():
        if(y == 1):
            l.append(x)
    return l
# print(unique([1, 1, 2, 3, 2, 4, 1, 5]))
# result: [3, 4, 5]