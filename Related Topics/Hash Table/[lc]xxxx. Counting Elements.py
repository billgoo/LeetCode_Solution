class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        c = 0
        for i in arr:
            if i + 1 in arr_set:
                c += 1
        return c