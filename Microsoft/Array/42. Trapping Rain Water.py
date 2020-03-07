class Solution:
    def trap(self, height: List[int]) -> int:
        """
        # dp O_n time and O_n space, three iterations
        # get list left_max and right_max
        # then we just need to add min(left_max[i], right_max[i]) - height[i]
        if not height:
            return 0
        
        n = len(height)
        left_max = height[:]
        right_max = height[:]
        
        for i in range(1, n):
            if left_max[i] < left_max[i - 1]:
                left_max[i] = left_max[i - 1]
                
        for i in range(n - 2, -1, -1):
            if right_max[i] < right_max[i + 1]:
                right_max[i] = right_max[i + 1]
                
        result = 0
        for i in range(n):
            result += min(left_max[i], right_max[i]) - height[i]
        
        return result
        """
        
        """
        # stack approach O_n time and O_n space, one pass
        # every pop add one of the sub areas
        stack = []
        result = 0
        n = len(height)
        
        for i in range(n):
            
            while stack and height[i] > height[stack[-1]]:
                # if current is larger than the top of stack
                # pop and calculate the area
                top = stack.pop()
                
                if not stack:
                    break
                    
                h = min(height[i], height[stack[-1]]) - height[top]
                result += h * (i - stack[-1] - 1)
                
            stack.append(i)
            
        return result
        """
        
        # two pointer O_n time and O_1 space and one pass
        # if there is a larger bar at one end (say right), 
        # we are assured that the water trapped would be dependant 
        # on height of bar in current direction (from left to right)
        # because left_max < right_max
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        
        result = 0
        
        while left < right:
            # one pass
            
            if height[left] < height[right]:
                # add left bar
                
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                    
                left += 1
                
            else:
                # add right bar
                
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                    
                right -= 1
        
        return result
    