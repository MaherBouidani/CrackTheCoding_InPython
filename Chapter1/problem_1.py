
#--------------Brute Force -------------
# string = "ab"
# isUnique = True

# #Edge Case: check if the string has a whitespace
# for char in string:
#     if char == " ": 
#         string = string.replace(" ", "")
    

# for i in range(len(string)): 
#     for j in range(i+1, len(string)):
#         if string[i] == string[j]:
#             isUnique = False
#             break
    
# if isUnique == True: 
#     print("String is Unique")
# else: 
#     print("String is not Unique")

# -------------------------------------------------

#--------------Using Set (Hash Table) -------------
string = "aBbcd"
isStringUnique = True
#Edge Case: check if the string has a whitespace
for char in string:
    if char == " ": 
        string = string.replace(" ", "")

if len(set(string)) == len(string) : 
    isStringUnique = True 
else: 
    isStringUnique = False

print(isStringUnique)

# -------------------------------------------------