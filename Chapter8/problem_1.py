def count_ways(steps, dicti={}):
    if steps < 0:
        return 0 
    elif steps == 0:
        return 1
    
    if steps not in dicti:
        dicti[steps] = count_ways(steps-1) + count_ways(steps-2) + count_ways(steps-3)
    
    print(dicti)
        

    return dicti[steps]


print(count_ways(10))