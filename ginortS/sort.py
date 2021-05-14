string = input()

small_list = []
cap_list = []
digit = []

def ginortS(small_list, cap_list, digit):

    for ele in digit:
        cap_list.append(ele)
    for i in cap_list:
        small_list.append(i)
    
    return(''.join(small_list))


for char in string:
    if char.islower():
        small_list.append(char)
    elif char.isupper():
        cap_list.append(char)
    elif char.isdigit():
        digit.append(char)

small_list = sorted(small_list)
cap_list = sorted(cap_list)
digit = sorted(digit)

print(ginortS(small_list, cap_list, digit))