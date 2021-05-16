if __name__ == '__main__':
    s = input()
    char_list = []

    for char in s:
        char_list.append(char)

    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False

    
    for ele in char_list:
        if ele.isalnum():
            alnum = True
        if ele.isalpha():
            alpha = True
        if ele.isdigit():
            digit = True
        if ele.islower():
            lower = True
        if ele.isupper():
            upper = True
    
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
