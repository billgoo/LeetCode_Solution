class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= (m * n)

        def reverse(start: int, end: int) -> None:
            while start < end:
                r, c, r_, c_ = start // n, start % n, end // n, end % n
                grid[r][c], grid[r_][c_] = grid[r_][c_], grid[r][c]
                start += 1
                end -= 1

        reverse(0, m * n - 1)
        reverse(0, k - 1)
        reverse(k, m * n - 1)

        return grid
