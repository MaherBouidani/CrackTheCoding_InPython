# def num(i):

#     if i == 1 :
#         factorial = max(1)
#     else:
#         factorial = max(i-1)


#     return i * factorial

# print(num(3))

def helper(start, end, row):
    for i in range(start, end, -1):
        print(row[i])
    
    return "Hey"



def test(row):

    start = 3
    end = 0

    left = helper(start, end, row)

    return left


test([1,2,3,4,5,6])