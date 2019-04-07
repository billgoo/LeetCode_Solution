import itertools
import copy
import collections

class Solution:
    def slidingPuzzle(self, board) -> int:
        q = collections.deque()
        s = set(tuple(itertools.chain(*board)))
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        if 0 in board[0]:
            index = (0, board[0].index(0))
        else:
            index = (1, board[1].index(0))
        q.append([(board, 0), index])
        
        target = [[1, 2, 3], [4, 5, 0]]
        while q:
            if len(s) == 720:
                return -1
            cur = q.popleft()
            node, step = cur[0]
            i, j = cur[1]
            if node == target:
                return step
            else:
                for n in neighbors:
                    temp = copy.deepcopy(node)
                    if 0 <= n[0] + i < 2 and 0 <= n[1] + j < 3:
                        x, y = n[0] + i, n[1] + j
                        temp[x][y], temp[i][j] = temp[i][j], temp[x][y]
                        
                        if tuple(itertools.chain(*temp)) not in s:
                            s.add(tuple(itertools.chain(*temp)))
                            q.append([(temp, step + 1), (x, y)])
        
        return -1
            


if __name__ == "__main__":
    print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))