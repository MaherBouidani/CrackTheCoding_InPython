from typing import List
from typing import List
from binary_matrix_module import BinaryMatrix
'''
Given a string message and an integer n, replace every nth consonant 
with the next consonant from the alphabet while keeping the case consistent 
(e.g. 'b' becomes 'c', 'x' becomes 'Y' etc.)

b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z
B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z

Example
For message "CodeSignal" and n = 3 and the output should be solution (message,n) = "CodeTignam"

'''


# class Solution: 

#     def fucntion_1(self, arr1, arr2, word):

#         self.Arr_1Length = len(arr1)
#         self.Arr_2Length = len(arr2)



#         self.backtrack(arr1, arr2, word)

    
#     def backtrack(self, arr1, arr2, word):

#         print(self.Arr_1Length)
#         print(self.Arr_2Length)


# sol = Solution()
# sol.fucntion_1([1,2,3,4,5], [6,7,8,9,10], "hello")

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    class Solution:
        # Import the BinaryMatrix class from the appropriate module
        class Solution:
            def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
                ROW, self.COL = binaryMatrix.dimensions()
                self.BINARY = binaryMatrix
                leftmostcol = self.COL
                for row in range(ROW):
                    ret = self.binary_search(row, 0, ROW)
                    leftmostcol = min(leftmostcol, ret)
                return leftmostcol

        def binary_search(self, row, left, right):
            if left > right:
                return float('inf')
            
            mid = left+right // 2 

            if self.BINARY.get(row, mid) == 0:
               return self.binary_search(row, mid+1, right)
            elif self.BINARY.get(row, mid) == 1:
                return min(mid, self.binary_search(row, left, mid-1))

    def binary_search(self, row, left, right):
        if left > right:
            return float('inf')
        
        mid = left+right // 2 

        if self.BINARY.get(row, mid) == 0:
           return self.binary_search(row, mid+1, right)
        elif self.BINARY.get(row, mid) == 1:
            return min(mid, self.binary_search(row, left, mid-1))
        

sol = Solution()
print(sol.leftMostColumnWithOne([[0,0],[1,1]]))