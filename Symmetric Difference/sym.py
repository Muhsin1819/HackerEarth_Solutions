#to find the symmetric difference between two sets..

def symmetric(lst):
    res = []
    fres = []
    for i in range(len(lst) - 1):
        temp = lst[i] ^ lst[i + 1]
        temp = list(temp)
        res.append(temp)
    for i in res:
        for j in i:
            fres.append(j)
    print(*fres)

n = int(input("Number of lists: "))
lst = []
for i in range(n):
    x = list(map(int, input().split()))
    lst.append(set(x))

symmetric(lst)
