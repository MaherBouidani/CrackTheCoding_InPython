# -------------------Brute ----------------
string1 = "apple"
string2 = "appless"
def one_way(string1, string2): 
    #Edge Case, Initial Check
    # if abs(len(string1) - len(string2)) > 1: 
    #     return False
    #----------------

    lis_ascii_1 = [0] * 128
    lis_ascii_2 = [0] * 128

    difference = []

    for letter in string1:
        lis_ascii_1[ord(letter)] += 1
    
    
    for letter in string2:
        lis_ascii_2[ord(letter)] += 1

    obj_zip = zip(lis_ascii_1, lis_ascii_2)

    for i, j in obj_zip:
        difference += [abs(i-j)] # or append
    
    print(difference)
    count = 0

    for item in difference:
        if item != 0:
            count += 1 
        if count > 1 or item ==2: 
            return False
    
    return True

print(one_way(string1, string2))
        
    
    



