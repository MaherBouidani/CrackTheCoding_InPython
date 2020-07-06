

def string_compression(string):
    str_new = ""
    for index1 in range(len(string)):
        count = 0
        for index2 in range(index1+1, len(string)):
            if string[index1] == string[index2]:
                count += 1
                flag += 1
            else:

                str_new += string[index1] + str(count)
                break
        

    return str_new

print(string_compression("aabbccc"))

            
                
            
        
            

