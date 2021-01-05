# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# 解法：看是否是有向无环图，使用拓扑排序
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
        queue = []
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
                
        while queue:
            c = queue.pop(0)
            for next_c in edges[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    queue.append(next_c)
            del edges[c]
            
        if len(edges) > 0:
            # have cycle
            return False
        else:
            return True

# Runtime: 96 ms, faster than 73.97% of Python3 online submissions for Course Schedule.
# Memory Usage: 15.5 MB, less than 80.81% of Python3 online submissions for Course Schedule.
                