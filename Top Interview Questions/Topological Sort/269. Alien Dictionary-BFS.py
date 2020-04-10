class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Write your code her
        if len(words) == 0:
            return ""
            
        # build graph
        G = dict()
        in_degree = {c: 0 for word in words for c in word}
        for word in words:
            for letter in word:
                if not letter in G:
                    G[letter] = set()
                    
        for first, last in zip(words, words[1:]):
            for i, j in zip(first, last):
                # len of last >= first, else it will break before
                # index out of range
                if i != j:
                    if not j in G[i]:
                        G[i].add(j)
                        in_degree[j] += 1
                    break
            else:
                if len(last) < len(first):
                    return ""
            
        # topological sort using BFS
        def topoSort():
            sequence = ""
            queue = [c for c in G if in_degree[c] == 0]
            
            # if len(queue) == 0:
            #     # have a circle
            #     return sequence
            while queue:
                node = queue.pop(0)
                sequence += node
                for v in G[node]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            # because G is DAG in this problem, no circle
            # don't need to del G[node]
            if len(sequence) < len(in_degree):
                return ""
            
            return sequence
            
        return topoSort()