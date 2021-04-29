def swapString(stringx):
    ordlist = []
    templist = []
    for i in stringx:
        ordlist.append(ord(i))
    for i in ordlist:
        templist.append(i)
    
    ordlist.sort()
    if ordlist == templist:
        return("NO")
    else:
        return("YES")


strings = list(map(str, input().split()))

flag = False

for i in strings:
    print(swapString(i))