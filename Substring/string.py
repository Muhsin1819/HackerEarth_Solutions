def count_substring(string, sub_string):
    len1 = len(string)
    len2 = len(sub_string)
    count = 0
    j = 0
    
    while j < len1:
        if string[j] == sub_string[0]:
            if string[j:j+len2] == sub_string:
                count += 1
        
        j += 1
    
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    print(count_substring(string, sub_string))
