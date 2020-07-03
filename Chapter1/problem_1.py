
#--------------Brute Force -------------
string = "ab"
isUnique = True

#Edge Case: check if the string has a whitespace
for char in string:
    if char == " ": 
        string = string.replace(" ", "")
    

for i in range(len(string)): 
    for j in range(i+1, len(string)):
        if string[i] == string[j]:
            isUnique = False
            break
    
if isUnique == True: 
    print("String is Unique")
else: 
    print("String is not Unique")

# -------------------------------------------------

#--------------Using Set (Hash Table) -------------
string = "aBbcd"
#Edge Case: check if the string has a whitespace
def isUnique(string):
    for char in string:
        if char == " ": 
            string = string.replace(" ", "")

    if len(set(string)) == len(string) : 
        return True
    else: 
        return False

print(isUnique(string))

# -------------------------------------------------

#--------------Using Bool -------------
string = "abbcd"
def isUnique(string): 
    if len(string) > 128: 
        return False
    
    bool_list = [None] * 128 

    for char in string: 
        val = ord(char)
        if bool(bool_list[val]):
            return False
        bool_list[val] = True
    
    return True
    
    
print(isUnique(string))

