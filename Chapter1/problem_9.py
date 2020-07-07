first_string = "maberbouidani"
second_string = "bouidanimaber"

def string_rotation(s1, s2):
    str_new =""
    for index in range(len(s1)):
        if s1[index] == s2[0] and s1[index-1] == s2[len(s2)-1]:
            str_new += s1[index:len(s1)] + s1[0:index]
            break
    
    if str_new == s2:
        return True
    else:
        return False

print(string_rotation(first_string, second_string))