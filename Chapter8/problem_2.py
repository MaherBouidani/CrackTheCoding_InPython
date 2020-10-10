def count_ways(r, c, dicti={}):
    
    if r == 0 or c ==0:
        return 0
    
    if r == 1 and c ==1:
        return 1

    dict_string = str(r) + str(c)

    if dict_string not in dicti:
       dicti[dict_string] = count_ways(r-1,c) + count_ways(r,c-1) + count_ways(r-1,c-1)
    
    print(dicti)
        

    return dicti[dict_string]


print(count_ways(2,3))


