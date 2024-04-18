class Solution:
    def pacificAtlantic(self, heights):

        '''
        we need to double check if there is a path from each cell to pacaific ocean and atlantic ocean

        The rule is: In order to have a path: the adjacent cell should equal or less than the current cell, 
        unless you are on the edge, there is always a path

        breaking point: there is a cell in which there is no path forward

        -North (upward) and West (left)is PO
        -South (downard) and East (right) is AO

        append the cell coordinate in the result list

        I am going to use DFS

        there is a potential opportunity for optimization

        '''

        result = []
        visit = set()

        def dfs(row, col, prev):


            if row < 0 or row > len(heights) - 1  or col < 0 or col > len(heights[0]) - 1:
                return True

            
            if heights[row][col] > prev or (row,col) in visit:
                return False

            visit.add((row, col))
            
            prev = heights[row][col]

            upward = dfs(row-1, col, prev)
            left = dfs(row, col-1, prev)
            right = dfs(row, col+1, prev)
            downward = dfs(row+1, col, prev)

            if upward and left:
                return True




            return (upward or left) and (right or downward)


        for row in range(len(heights)):

            for col in range(len(heights[row])):
                visit.clear()

                ret = dfs(row, col, heights[row][col])

                if ret:
                    result.append([row,col])
        
        return result 
    

    

sol = Solution()
print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

print("I am here")
        