class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        - we create adj list for every course, the value would be the prereqs, this is the direct list
        - and we append to that global map the course: prereqs of each value both direct and indirect
        - then for queries we ask if the course is in the global map or not
        - complexity
            - time = 
            - space = 
        """
        #adjacency list and global map
        map = {i: [] for i in range(numCourses)}
        for pre, course in prerequisites:
            map[course].append(pre)
        global_map = {}

        #dfs to gather the prereqs
        def dfs(course):
            #base/exit
            if course in global_map:
                return global_map[course]
            
            #store + explore
            prereq = set()
            for pre in map[course]:
                prereq.add(pre) #adding courses from the map
                prereq.update(dfs(pre)) #adding prereqs of prereqs using the dfs
            
            #return
            global_map[course] = prereq #adding to the global map
            return global_map[course]

        #populate the global map
        for course in range(numCourses):
            dfs(course)

        #answering the queries
        answer = []
        for u, v in queries:
            if u in global_map[v]:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer


        