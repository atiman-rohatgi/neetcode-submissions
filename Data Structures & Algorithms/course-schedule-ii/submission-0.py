class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        - dfs, but we will store the courses taken in order from normal course question
        - have an adjacenecy list, with course : prereq
            - dfs course wise, with their pre reqs and take them in order to satisfy the first course req
            - basically have two sets, visited for the path to detect cycles
            - and a completed if the path is clear so that we can mark in order
        - complexity
            - time = O(v+e)
            - cpace = O(v+e)
        - a different aprroach is bfs way, which means we take the empty courses first, and mark the courses free that depeneded upon these and this way we take all of them if a course is left then not possible.
        """

        #adjacency list
        map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            map[course].append(pre)

        #set things up
        visited = set()
        completed = set()
        output = []

        #dfs
        def dfs(course):
            #exit
            if course in completed:
                return True
            if course in visited:
                return False

            #store
            visited.add(course)

            #explore
            for pre in map[course]:
                if dfs(pre) == False:
                    return False

            #backtrack
            visited.remove(course)
            completed.add(course)
            output.append(course)

            #return
            return True

        #main loop
        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return output
        