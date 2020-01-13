class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        # O(n^2) method as the normal 3Sum question
        # time limit exceeded
        """
        MOD = 10 ** 9 + 7
        re = 0
        A.sort()
        
        for i in range(len(A)):
            T = target - A[i]
            l, r = i + 1, len(A) - 1
            
            # two sum method
            while l < r:
                if A[l] + A[r] < T:
                    l += 1
                elif A[l] + A[r] > T:
                    r -= 1
                else:
                    if A[l] != A[r]:
                        # count same elements for left and right elements
                        j = k = 1
                        while l + 1 < r and A[l] == A[l + 1]:
                            j += 1
                            l += 1
                        while l + 1 < r and A[r] == A[r - 1]:
                            k += 1
                            r -= 1
                        re += j * k
                        l += 1
                        r -= 1
                    else:
                        # range(l, r) contains the same number
                        # so we use binomial formula
                        re += (r - l + 1) * (r - l) // 2
                        break
                # re %= MOD
            # while ends
        # for ends
            
        re %= MOD
        return int(re)
        """
        # 3 cases covers all possible combination:
        # i == j == k
        # i == j != k
        # i < k && j < k
        # time O(n + m^2), space O(m), m is the number of numbers
        c = collections.Counter(A)
        re = 0
        
        for i in c:
            for j in c:
                if j >= i:
                    k = target - i - j
                    
                    # binomial formula
                    if i == j == k:
                        re += c[i] * (c[i] - 1) * (c[i] - 2) // 6
                    elif i == j != k:
                        re += c[i] * (c[i] - 1) * c[k] // 2
                    elif k > i and k > j:
                        re += c[i] * c[j] * c[k]
                        
        return re % (10**9 + 7)
        