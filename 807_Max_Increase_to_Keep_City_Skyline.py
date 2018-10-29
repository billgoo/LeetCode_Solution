class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]
        skyline_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                skyline_sum += (min(row_max[i], col_max[j]) - grid[i][j])
        return skyline_sum


if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    s = Solution()
    sol = s.maxIncreaseKeepingSkyline(grid)
    print(sol)
