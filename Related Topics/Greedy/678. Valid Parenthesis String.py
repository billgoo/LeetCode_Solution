class Solution:
    def checkValidString(self, s: str) -> bool:
        # use two stack O_n time and O_n space
        """
        # to check if ), pop from left or star
        #     if nothing to pop, return False
        # if after loop, we then use a loop to check the
        #     top of left and star, if we encounter a top of
        #     left is at the right of top of star, return False
        # And also if at the end of the function, the left is not
        #     empty, return False else True
        
        left_count = []
        star_count = []
        for i in range(len(s)):
            if s[i] == '(':
                left_count.append(i)
            elif s[i] == '*':
                star_count.append(i)
            elif s[i] == ')':
                if len(left_count) > 0:
                    left_count.pop()
                elif len(star_count) > 0:
                    star_count.pop()
                else:
                    return False
            # print(left_count, star_count)
            
        while len(left_count) > 0 and len(star_count) > 0:
            if left_count.pop() > star_count.pop():
                return False
            
        return len(left_count) == 0
        """
        
        # O_n time and O_1 space greedy
        # lo and hi represent the possible least and most amount
        #     of ( at current state
        # if (, lo++; if ), hi--
        # if hi < 0 or at the end of loop we have lo > 0, return False
        
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
            else:
                lo = max(lo - 1, 0)
                
            if c != ')':
                hi += 1
            else:
                hi -= 1
            
            if hi < 0:
                return False
        
        return lo == 0