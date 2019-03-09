class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 2:
            return len(tree)
        
        blocks = []
        temp, c = tree[0], 1
        for i in range(1, len(tree)):
            if tree[i] != temp:
                blocks.append([temp, c])
                temp, c = tree[i], 1
            else:
                c += 1
            if i == len(tree) - 1:
                blocks.append([temp, c])
                break
                
        result = k = 0
        while k < len(blocks):
            types, weight = set(), 0
            
            for j in range(k, len(blocks)):
                types.add(blocks[j][0])
                weight += blocks[j][1]
                
                if len(types) > 2:
                    k = j - 1
                    break
                result = max(result, weight)
                if j == len(blocks) - 1:
                    return max(result, weight)
                
        return result
                