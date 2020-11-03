l = int(input())
n = int(input())
for i in range(n):
    d = list(map(int, input().split()))
    w = d[0]
    h = d[1]
    if w<l:
        print('UPLOAD ANOTHER')
    elif h<l:
        print('UPLOAD ANOTHER')
    elif w==h:
        print("ACCEPTED")
    else:
        print("CROP IT")
