# def lengthOfLongestSubstring(s: str):
#         N = len(s)
    

#         if N <= 1:
#             return 0
#         result = []
#         longest_length= 0

        
#         for i in range(N):
            
#             j = i+1
#             print("i:", i)
        
#             for j in range(N):
               
#                 substring = s[i:j]
#                 if j == N-1 and (s[j] not in substring):
#                     result.append(s[i:])
                
#                 if s[j] in substring:
#                     result.append(substring)
#                     break
#                 print("j:", j)
        
#         for string in result:
#             if len(string) > longest_length:
#                 longest_length = len(string)
#         print(result)
       
#         return longest_length

# print(lengthOfLongestSubstring("au"))

# dicts = {}

# dicts[0] = 1
# dicts[0] = 1

# print(dicts)

# def f(x):
#     x = 8

# x=6

# f(x)

# print("This is \x61 \npython interview")
# print(r"This is \x61 \ngood interview")
# print(x)

# lis = ["test1", "test2", "test2"]

# dic = {}

# for position in lis: 
#     dic[position] = 2

# print(dic)

# s = "abcd"

# print(s.find('b'))
# def lucky(n):
#     s = n 
#     lucky_num = n
#     i = 1 
#     while i <= s:
#         # print("s:", s)
#         if '4' in str(i):
#             s += 1 
#             lucky_num += 1
#             # print("test")
#         if '13' in str(i):
#             s += 1 
#             lucky_num += 1

       
#         i = i+1
#         # print("i:", i)
       

#     return lucky_num

# print(lucky(12))

def comb(arr):
    prev = arr[0]
    current = 1 

    res = []

    for i in range(1, len(arr[1:])+1):
        if prev == arr[i]:
            current +=1 
            
        else:
            if current == 1:
                res.append(prev)
                prev = arr[i]
            else:
                res.append(str(prev) +":"+ str(current))
                current = 1
                prev = arr[i]
        print(i)
        
    if current == 1:
                res.append(prev)
                prev = arr[i]
    else:
                res.append(str(prev) +":"+ str(current))
                current = 1
                prev = arr[i]
                
    return res

print(comb([5,5,5,7,7,3,2,2]))




