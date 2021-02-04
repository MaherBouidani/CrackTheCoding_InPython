# def check_palin(word):

#     if len(word) % 2 ==1:
#         middle = len(word)//2

#         for i in range(middle, len(word)):
#             if word[i] is not word[middle - abs(middle-i)]:
#                 return False
        
#         return True
#     elif len(word) % 2 == 0:
#         start = 0
#         middle = len(word)//2
#         for j in range (len(word)-1, middle - 1, -1):
#             if word[j] is not word[start]:
#                 return False
#             start += 1 
        
#         return True
def palin(word, start, end): 

    return word[start+1:end]
    


def check_palin(word):
    start = 0 
    end = len(word) -1

    if word[start] != word[end]:
        return False
    else: 
        word = palin(word, start, end)
        print(word)
        if len(word) == 0: 
            return True
        else:
            print(check_palin(word))


    
    

check_palin("taeaeat")


 