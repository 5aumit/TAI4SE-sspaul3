from typing import List 

class CourseSchedule:
    """
    Problem: Course Schedule (#207)
    Key Insights:
    1. Create adjaceny list of courses to prerequisites.
    2. Use DFS and visited set to detect a cycle. If there is a cycle, cannot finish all the courses.
    3. Remember to remove a course (node) from visited set if that course is "cleared" (able to take the course). 
    4. Note that this is not a cycle (so if don't remove node in step 3, would incorrectly identify this as a cycle):
        1 -> 2 -> 3 
        2 -> 4 -> 3 
    More info: 
    1. Concept of Topological order: for an edge uv, u must always come before v (so no cycles where v also comes before u)

    Time Complexity:
    O(V + E):
    1. Create pre_map: O(P), P: prerequisites
        a. We're iterating through the list of prereqs 
    2. Call dfs: O(C), C: courses
        a. We're iterating through all the courses once  
    3. dfs: O(V + E)
        a. We visit each course and each edge at most once

    Space Complexity: O(V + E)
    1. Create pre_map: O(V + E), V: courses, E: prereqs
    2. dfs call stack: O(V + E) 
    """
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visited_set = set()

        def dfs(crs):
            if crs in visited_set:
                return False
            if pre_map[crs] == []:
                return True
            visited_set.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visited_set.remove(crs)
            pre_map[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True 
    