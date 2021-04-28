def duration(n):
    for i in range(n):
        lst = list()
        sh, sm, eh, em = map(int, input().split())
        rsh = sh * 60
        reh = eh * 60
        mout = (reh + em) - (rsh + sm)
        hour = mout // 60
        lst.append(hour)
        minute = mout % 60
        lst.append(minute)
        print(' '.join(map(str, lst)))


n = int(input())
duration(n)
