# class Graph:
#     def __init__(self) -> None:
#         self.vertices = {}

#     def add_vertices(self, vertix):
#         if vertix not in self.vertices:
#             self.vertices[vertix] = set()

#     def add_edges(self, vertix, edge):
#         if vertix in self.vertices and edge in self.vertices:
#             self.vertices[vertix].add(edge)

#     def remove_vertix(self, vertix):
#         if vertix in self.vertices:
#             del self.vertices[vertix]
        
#             for value in self.vertices.values():
#                 if vertix in value:
#                     value.remove(vertix)
    
#     def dfs_helper(self, vertix, visited):
#         print(".............................")
#         print("visited BEFORE ADD", visited)
#         if vertix not in visited:
#             visited.add(vertix)
        
#         print("visited AFTER ADD", visited)
#         print(".............................")
        
#         for neighbour in self.vertices[vertix]:
#             if neighbour not in visited:
#                 self.dfs_helper(neighbour, visited)



#     def dfs_traversal(self, vertix):
#         visited = set()

#         self.dfs_helper(vertix, visited)

#         print(visited)










# graph = Graph()

# graph.add_vertices('A')
# graph.add_vertices('B')
# graph.add_vertices('C')
# graph.add_vertices('D')

# graph.add_edges('A', 'B')
# graph.add_edges('A', 'C')

# graph.add_edges('B', 'D')
# graph.add_edges('B', 'C')

# graph.add_edges('C', 'D')

# graph.add_edges('D', 'A')

# graph.dfs_traversal('A')


# print(graph.vertices)

# def make_list(num): 
#     if num == 1:        
#         return 1    
#     return [num].append(make_list(num - 1))
	    
        
            
    # print(make_list(5))

# s = [1]
# s.append(3)

# print(s)
# s = [[1,0], [2,3], [4,5]]

# for row, item in s:
#     print("row:", row, "....", "item:", item)

# from collections import defaultdict


# dictionary = defaultdict(list)

# dictionary[0].append(1)

# for item in dictionary[2]:
#     print("I am here")

# print(dictionary)

# list_test = [1,2,3,4]

# print(list_test[len(list_test) - 1])

# a = None
# b = 1

# if b > a:
#     print("a evalutes to 0 during integer comparission")

nums = [1,2,3,4]

# if 3 in nums[2:]:
#     print("h")

# print(nums[2:])

# my_dict = {"a": 1, "b": 2, "c": 3}

# print(my_dict.keys(), type(list(my_dict.keys())))

# a = [1,2]

# print(a[0:3])


# def dfs(nums): 
    

#     left = dfs(nums)




# dfs(nums)


# print(3%2)

# def can_attend_meetings(intervals):
#         # Write your code here

#         # Big(O) is n log(n) since we do sorting.

#         if len(intervals) == 1: 
#             return 1

#         intervals.sort()
#         num_rooms = 1

#         print(intervals)

#         for time in range(1,len(intervals)):
#             start_time = intervals[time][0]
#             end_time = intervals[time-1][1]

#             if start_time > end_time:
#                 continue
#             else:
#                 num_rooms += 1
                
        
#         return num_rooms

# print(can_attend_meetings([(0,30),(5,10),(15,20),(16,23), (25,28)]))

# class Solution:

#     def encode(self, strs):
#         encoded_list = []

#         for item in strs: 
#             item_encode = ''.join([str(ord(char)) + '_' for char in item])
#             encoded_list.append(item_encode)
#             encoded_list.append("$")
        
#         del encoded_list[len(encoded_list)-1]
#         print(encoded_list)

#         return ''.join(encoded_list)
    
#     def decode(self, s):
#         decoded= []
#         string_split = s.split("$")
#         print(string_split)

#         for item in string_split:
#             item_split = item.split('_')
#             del item_split[len(item_split)-1]
#             print(item_split)
#             item_decode = ''.join([chr(int(itm)) for itm in item_split])
#             decoded.append(item_decode)
        
#         return decoded

# sol = Solution()
# list_example = ["we","say",":","yes"]
# encoded = sol.encode(list_example)
# decoded = sol.decode(encoded)
# print(list_example == decoded)


# list_example = [1,2,3,4]
# modified = [list_example[index] for index in range(len(list_example)) if index < len(list_example) - 1]

# modified = list_example[:- 1]

# print("empty list example", list_example)
# print("modified list", modified)

# list_example = modified
# print("new list example", list_example)


# class Solution:
#     def canPlaceFlowers(self, flowerbed, n):
#         '''
#         1. valid flower if there 0s its adjacents
#             1.1. when you visit a cell, see its right and left, if zero: deduct from n, otherwise continue. 
#             if n becomes 0, true, otherwise false

#             1.2 special case: when you are at the first element (you look right), or at the last element (you look left)
#         '''

#         if len(flowerbed) == 1 and flowebed[0] == 0 and n == 1:
#             return True
#         elif len(flowerbed) == 1 and flowebed[0] == 1 and n >= 1:
#             return False


#         for index in range(len(flowerbed)):

#             if index == 0 and flowerbed[index] == 0: 
#                 if flowerbed[index+1] == 0:
#                     n = n-1
#                     flowerbed[index] = 1
#             elif index == len(flowerbed) - 1 and flowerbed[index] == 0 and n != 0:
#                 if flowerbed[index - 1] == 0:
#                     n = n-1
#                     flowerbed[index] = 1
#             elif 0 < index < len(flowerbed) - 1 and flowerbed[index] == 0 and flowerbed[index - 1] == 0 and flowerbed[index + 1] ==0:
#                 print(index, flowerbed[index])
#                 n = n-1
#                 flowerbed[index] = 1
        
#         if n == 0:
#             return True
#         else:
#             return False

# sol = Solution()

# result = sol.canPlaceFlowers([1,0,0,0,1], 1)

# print("result", result)




# This is the right way to unpack itterable object
# example_list = [[0,1,3], [2,4,6], [6,8,10], [10,18,2]]


# for a, b in example_list: 
#     print(a,b)

# The wrong way to do it: 

# sum_var = 0 

# for a,b,c in example_list:
#     sum_var += a

# print(sum_var)

# print(sum(a for a,b,c in example_list))
'''
    house_trades:
    [
    "AAPL,B,0100,ABC123",
    "AAPL,B,0100,ABC123",
    "GOOG,S,0050,CDC333"
    ]

    // street_trades:
    [
    " FB,B,0100,GBGGGG",
    "AAPL,B,0100,ABC123"
    ]

    We would expect the following output:

    [
    " FB,B,0100,GBGGGG",
    "AAPL,B,0100,ABC123",
    "GOOG,S,0050,CDC333"
    ]
'''

# check best practices for naming.

# import copy

# class Solution: 
        

#     def findMatchedTrades(self, htrades, strades):
#         h_dict = {}
#         s_dict = {}
#         matched = {}

#         for h_trade in htrades:
#             if h_trade in h_dict:
#                 h_dict[h_trade] += 1
            
#             h_dict[h_trade] = 1
        
#         for s_trade in strades:
#             if s_trade in s_dict:
#                 s_dict[s_trade] += 1
            
#             s_dict[s_trade] = 1

#         for k,v in h_dict.items():
#             if k in s_dict:
#                 matched[k] = min(v, s_dict[k])
            
#         return matched
    
#     def unMatchedTradesHelper(self, htrades, strades):

#         matched_trades = self.findMatchedTrades(htrades, strades)
#         matched_trades_copy = copy.deepcopy(matched_trades)
#         unmatched_htrades = []
#         unmatched_strades = []

#         for item in htrades:
#             if item in matched_trades and matched_trades[item] != 0:
#                 matched_trades[item] -= 1
#             else:
#                 unmatched_htrades.append(item)
        
#         for item in strades:
#             if item in matched_trades_copy and matched_trades_copy[item] != 0:
#                 matched_trades_copy[item] -= 1
#             else:
#                 unmatched_strades.append(item)
        
#         return unmatched_htrades, unmatched_strades



#     def findUnmatchedTrades(self, htrades, strades):

#         # matched_trades = self.findMatchedTrades(htrades, strades)
#         # matched_trades_copy = copy.deepcopy(matched_trades)
#         # print("matched_trades", matched_trades)
#         # unmatched_htrades = []
#         # unmatched_strades = []

#         # for item in htrades:
#         #     if item in matched_trades and matched_trades[item] != 0:
#         #         matched_trades[item] -= 1
#         #     else:
#         #         unmatched_htrades.append(item)
        
#         # for item in strades:
#         #     if item in matched_trades_copy and matched_trades_copy[item] != 0:
#         #         matched_trades_copy[item] -= 1
#         #     else:
#         #         unmatched_strades.append(item)
#         unmatched_htrades, unmatched_strades = self.unMatchedTradesHelper(htrades,strades)

#         return unmatched_htrades + unmatched_strades


#     def fuzzyMatchHelper(self, htrades, strades):

#         unmatched_htrades, unmatched_strades = self.unMatchedTradesHelper(htrades,strades)

#         fuzzy_dict_htrades= {}
#         fuzzy_dict_strades = {}

#         for item in unmatched_htrades:
#             new_item = item.split(',')
#             del new_item[-1]
#             string_item = ','.join(new_item)
                
#             fuzzy_dict_htrades[item] = string_item
            

#         for item in unmatched_strades:
#             new_item = item.split(',')
#             del new_item[-1]
#             string_item = ','.join(new_item)
                
#             fuzzy_dict_strades[item] = string_item
        
#         fuzzy_htrades = []
#         fuzzy_strades = []

#         for value in fuzzy_dict_htrades.values():
#             fuzzy_htrades.append(value)

#         for value in fuzzy_dict_strades.values():
#             fuzzy_strades.append(value)
        
#         unmatched_fuzzy_htrades, unmatched_fuzzy_strades = self.unMatchedTradesHelper(fuzzy_htrades, fuzzy_strades)

#         result = []

#         for item in unmatched_fuzzy_htrades:
#             k = next(key for key, value in fuzzy_dict_htrades.items() if value == item)
#             result.append(k)
        
#         for item in unmatched_fuzzy_strades:
#             k = next(key for key, value in fuzzy_dict_strades.items() if value == item)
#             result.append(k)

#         return result



# sol = Solution()
# house_trades = [
# "AAPL,B,0100,ABC123",
# "AAPL,S,0200,ABC456",
# "AAPL,S,0200,ABC987",
# "GOOG,S,0050,CDC333"
# ]
# street_trades = [
# "FB,B,0100,GBGGGG",
# "AAPL,S,0200,ABC264",
# ]
# result_exact = sol.findUnmatchedTrades(house_trades, street_trades)
# print("exact", result_exact)
# result_fuzzy = sol.fuzzyMatchHelper(house_trades,street_trades)
# print("fuzzy", result_fuzzy)



# class TreeNode: 
    
#     def __init__(self, val= 0, left= None, right =None):
#         self.value = val
#         self.left = left
#         self.right = right



# root = TreeNode(9)
# root.left = TreeNode(10)
# root.right = TreeNode(4)

# print(root.self)


example_list = [1,2,3,4,5]

temp = example_list.remove(1)

print(temp)
print(example_list)











