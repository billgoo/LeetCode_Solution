class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # qucik select
        def select(left, right, k_):
            if left == right:
                return nums[left]
            
            i = random.randint(left, right)
            i = partition(left, right, i)
            
            if k_ == i:
                return nums[i]
            elif k_ > i:
                # right part
                return select(i + 1, right, k_)
            else:
                # left part
                return select(left, i - 1, k_)
            
        def partition(left, right, i):
            nums[i], nums[right] = nums[right], nums[i]
            
            j = left
            for k in range(left, right):
                if nums[k] < nums[right]:
                    nums[j], nums[k] = nums[k], nums[j]
                    j += 1
                    
            nums[right], nums[j] = nums[j], nums[right]
            return j
        
        return select(0, len(nums) - 1, len(nums) - k)