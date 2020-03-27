/**
 * Description
 * Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.
 */

public class Solution {
    /*
     * @param A: An integer array.
     * @return: nothing
     */
    public void rerange(int[] A) {
        // write your code here
        Arrays.sort(A);
        int l = 0, r = A.length - 1;
        
        if (A.length % 2 == 0) {
            l++;
            r--;
        }
        else if (A[A.length >>> 1] > 0) {
            // 正数多
            r--;
        }
        else {
            // 负数多
            l++;
        }
        
        while (l < r) {
            int temp = A[l];
            A[l] = A[r];
            A[r] = temp;
            l += 2;
            r -= 2;
        }
    }
}