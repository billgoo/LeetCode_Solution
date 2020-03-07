class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d = {i: 1 for i in arr1}
        for i in arr2:
            if i in d:
                d[i] += 1
        for i in arr3:
            if i in d:
                d[i] += 1
        return [i for i in d if d[i] == 3]
        