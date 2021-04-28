#function_definition
def zoo(str_small):
    countz = 0
    counto = 0
    for i in str_small:
        if(i == 'z'):
            countz += 1
        elif(i == 'o'):
            counto += 1
        else:
            return("Invalid input")
    if(counto == 2*countz):
        return("Yes")
    else:
        return("No")

#receiving_input
str = input()
str_small = str.lower()

#calling_function
print(zoo(str_small))
