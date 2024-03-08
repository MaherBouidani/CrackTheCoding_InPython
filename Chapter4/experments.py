# import collections

# items = [1,2,3,4,5,6]
# root = items[0]
# q = collections.deque()
# q.append(root)

# entry = 1
# while q:
#     print("entry:", entry)
#     entry += 1

#     if entry == 9:
#         break

#     for i in range(len(q)):
#         itm = q.popleft()
#         print(itm)
#         q.append(items[1])

# You are given an array A of N non-negative integers and an integer K. 
# You can perform the following operation on this given array any number of times:
# • Choose an index i (1<=i<=N), and increase the element at this index by 1

# Task Determine the minimum number of operations that needs to be performed, 
# so that every subarray of size 3 or more has a maximum element, greater than or equal to K

# Example:
# n=4
# k=5
# a = [2,1,1,3] subarrays: guaranteed [2,1,1,3] 

# [2,1,1], [1,1,3], index:1 and 2

# [2,1,1,3,4,1,1,2,3] ......[2,1,1], [1,1,3], [1,3,4], [3,4,1], [4,1,1], [1,1,2], [1,2,3]
#                              4 operations     2operations   1 operations 4 operations    min_operations: 11 operations

# 1 - create all possible subarrays such every subarray has common elements to the next one
# 2 - find the common elements and choose the one that is closer to K 
#     edge_case: if the common element K or over is already there, skip the operations (3)
# 3 - perform num_operations on the given element to bring it to K or over 
# 4 - continue to do this for all other subarrays
# 5 - return the number_operations

# potential_hypothesis: I might not need to generate all arrays before hand. (this hypothesis to be verified)

# [1,2,3,4,5,6], [1,2,3] [2,3,4]

# [1,2,3,4]

                           


# ops: [2,2,2,3]
# [2,3,3,3]
# [2,4,4,3]
# [2,5,5,3]

# ans = 4

# [1,2,3,4,5], [1,2,3], [2,3,4], [2,3,4], [3,4,5]
#              [2,3,4]  [3,4,5]

def helper(arr, index, k):
    operations_on_elements = k - arr[index]
    return operations_on_elements
    

def find_maximum_operations(arr, k):
    max_operations = 0

    number_subarrays_size_3 = len(arr) - 2

    for j in range(1, number_subarrays_size_3):

        if arr[j] >= arr[j+1]:
            max_between_common_elements = arr[j]
            index = j
        else:
            max_between_common_elements = arr[j+1]
            index = j+1

        if max_between_common_elements < k:
            operations = helper(arr, index, k)
            max_operations += operations

    return max_operations


a = []

# j=1, arr[1] = 2, arr[2] = 3, 
# max_between_elements = arr[2], index = 2 
# k =5, operations_on_elements = 5 - 3 = 2 
# max_operations = 2

# j = 2, arr[2] = 3, arr[3] = 4
# max_between_elements = arr[3], index = 3
# k =5, operations_on_elements = 5 - 4 = 1
# max_operations = 3


print(find_maximum_operations(a,5))




            



