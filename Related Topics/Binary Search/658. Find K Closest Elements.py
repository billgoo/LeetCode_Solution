class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or k == 0:
            return []
        
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        
        n = len(arr)
        
        # bi-search
        l, r = 0, n - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == x:
                i = m
                break
            elif arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        
        if i == -1:
            if abs(arr[l] - x) < abs(arr[r] - x):
                i = l
            else:
                i = r
                
        l, r = max(0, i - k + 1), min(n - 1, i + k - 1)
        while r - l > k - 1:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
                
        return arr[l:r+1]
        