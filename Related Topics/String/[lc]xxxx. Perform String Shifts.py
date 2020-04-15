"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
"""

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        """
        Step 1:
        Becasue for length n string, do left shift i is to do the right shift n - i. 
        We can just use mod to change both left and right shift to left shift and suppose 
        we have shift amount for left shift to be positive and for right shift to be negative.

        Step 2:
        So for both shifting, we just need to concate the string s[shift : n-1] and s[0 : shift] 
        regardless the positive or negative status of shift.

        And in the first we will always have positive shift amount for left shift, 
        so we can just do the step 2.
        """
        n = len(s)
        
        final_shift = sum([x[1] if x[0] == 0 else -x[1] for x in shift]) % n
        
        if final_shift != 0:
            return s[final_shift :] + s[:final_shift]
        
        return s