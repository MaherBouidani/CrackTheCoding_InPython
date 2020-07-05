
# ----------- Brute Force -----------------
string = ' John Smith '
def space_replacement(stirng):
    str_new = ''
    for index in range(len(string)):
        if string[index] == ' ':
           str_new += '20%'
        else:
           str_new += string[index]
    return str_new 


print(space_replacement(string))

