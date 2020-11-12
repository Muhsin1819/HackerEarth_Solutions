def pairs(len, strl):
    count = 0
    for i in range(len-1):
        if ((strl[i + 1] in vowels) and (strl[i] not in vowels)):
            count += 1
    print(count)


vowels = ['a','e','i','o','u']
test_cases = int(input())
for i in range(test_cases):
    len = int(input())
    str = input()
    strl = str.lower()
    pairs(len, strl)
