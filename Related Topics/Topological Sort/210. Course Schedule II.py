# There are a total of n courses you have to take labelled from 0 to n - 1.
# Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
# Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
# If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
# 解法：看是否是有向无环图，使用拓扑排序，同 lc.207
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init graph
        indegree = [0 for _ in range(numCourses)]
        edges = {}
        for i in range(numCourses):
            edges[i] = []
        
        # build graph
        for e in prerequisites:
            edges[e[1]].append(e[0])
            indegree[e[0]] += 1
        
        # topo sort using BFS
        result = []
        queue = []
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
        
        while queue:
            c = queue.pop(0)
            result.append(c)
            for next_c in edges[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    queue.append(next_c)
            # del edges[c]
            
        if len(result) != numCourses:
            # have cycle
            return []
        else:
            return result

# Runtime: 100 ms, faster than 61.89% of Python3 online submissions for Course Schedule II.
# Memory Usage: 15.3 MB, less than 91.47% of Python3 online submissions for Course Schedule II.
                