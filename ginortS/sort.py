string = input()

small_list = []
cap_list = []
digit = []
odd_digit = []
even_digit = []

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

for num in digit:
    if int(num)%2 == 0:
        even_digit.append(num)
    else:
        odd_digit.append(num)

even_digit = sorted(even_digit)
odd_digit = sorted(odd_digit)

for t in even_digit:
    odd_digit.append(t)


print(ginortS(small_list, cap_list, odd_digit), end="")