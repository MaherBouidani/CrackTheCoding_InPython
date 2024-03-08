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

def solution(rh_users, new_users):
    referral = {}
    relationship = {[]}

    for index, user in enumerate(rh_users):
        if user in referral:
            referral[user] += 1
        
        referral[user] = 1

        if new_users[index] in rh_users:
            appearness_times = rh_users.count(new_users[index])
            referral[user] += appearness_times
        
        
        if user in relationship:
            relationship[user].append(new_users[index])
        
        relationship[user] = []
        


        #How to map out the relationship
    
    return referral


result = solution(["A", "B", "C"], ["B", "C", "D"])

print(result)

