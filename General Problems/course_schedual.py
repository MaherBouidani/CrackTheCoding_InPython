def findOrder(numCourses, prerequisites):

    courseToPrereq = {i : [] for i in range(numCourses)}

    for course, prereq in prerequisites:
        courseToPrereq[course].append(prereq)

    visitedCourses = set()
    result = []

    def dfs(course):
        
        if courseToPrereq[course] == []:
            result.append(course )
            return True
        
        if course in visitedCourses:
            return []

        
        visitedCourses.add(course)

        for prereq in courseToPrereq[course]:

            if not dfs(prereq): return []
        
        visitedCourses.remove(course)
        courseToPrereq[course] = []
        result.append(course)

        return True
    
    for crs in range(numCourses):
        if not dfs(crs): return []
    
    return result


print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))