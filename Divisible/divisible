def divisible(n, arr):
    lst1 = list()
    lst2 = list()
    for i in range(n):
        if(i < n/2):
            while arr[i] >= 10:
                arr[i] = arr[i]//10
            lst1.append(arr[i])
        else:
            lst2.append(arr[i] % 10)

    res = lst1 + lst2
    fres = int("".join(map(str, res)))

    if((fres % 11) == 0):
        print('OUI')
    else:
        print('NON')



n = int(input())
arr = list(map(int, input().split()))

divisible(n, arr)
