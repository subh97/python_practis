def duplicate_string(str,n):
    index = 0
     
    # Traverse through all characters
    for i in range(0, n):
         
        # Check if str[i] is present before it
        for j in range(0, i + 1):
            if (str[i] == str[j]):
                break
                 
        # If not present, then add it to
        # result.
        if (j == i):
            str[index] = str[i]
            index += 1
             
    return "".join(str[:index])
 

str= "abbabcdabbdadd"
n = len(str)
print(f"print orginal string :: {str}")
print(duplicate_string(list(str), n))