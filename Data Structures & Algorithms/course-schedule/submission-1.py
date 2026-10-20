class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - this is us detecting cycle
        - create a dict with courses and their pre reqs
            - dfs index wise and maintin a a path set, if any in path already hence a cycle
        - we have 2 exit condition either safe if empty set or cycle 
        - we backtrack and then continue
        - complexity
            - time = O(V+E)
            - space = O(V+E)
        """

        #adjacency list
        map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            map[course].append(pre)

        #visited set
        visited = set()

        #dfs + backtrack
        def dfs(course):
            #exit condition
            if course in visited:
                return False
            if map[course] == []:
                return True

            #visited
            visited.add(course)

            #recurse
            for pre in map[course]:
                if dfs(pre) == False:
                    return False

            #pop to backtrack
            visited.remove(course) #to reset
            map[course] = []#mark safe

            return True # if all good, then return True

        #main loop
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        
        return True
        
        