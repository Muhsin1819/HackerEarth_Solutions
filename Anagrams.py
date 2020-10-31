from collections import Counter

for _ in range(int(input())):
    a = Counter(input())
    b = Counter(input())

    print(sum((a-b).values()) + sum((b-a).values()))
