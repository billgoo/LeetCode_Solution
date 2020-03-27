import java.util.Arrays;

/**
 * 描述
 * 
 * 给一组整数，问能找出多少对整数，他们的和大于一个给定的目标值。
 * 
 * 样例
 * 
 * 对于 numbers =[2, 7, 11, 15], target =24的情况，返回1。因为只有11 + 15可以大于24。
 * 
 * 挑战
 * 
 * Do it in O(1) extra space and O(nlogn) time
 * 
 * 思路
 * 
 * 两数之和典型的follow up题，本题是寻找大于target的情况，固定右指针，观察左指针的变化， 找到第一个满足大于target的指针后，right
 * - left即可得数组中对于当前right所有满足条件的组合个数； 然后right--，右指针左移计算新的位置满足大于target的组合的个数
 */
class Solution {
    /**
     * @param nums: an array of integer
     * @param target: an integer
     * @return: an integer
     */
    public int twoSum2(int[] nums, int target) {
        if (nums == null || nums.length < 2) {
            return 0;
        }
        
        Arrays.sort(nums);
        
        int left = 0, right = nums.length - 1;
        int count = 0;
        while (left < right) {
            if (nums[left] + nums[right] <= target) {
                left++;
            } else {
                count += right - left;
                right--;
            }
        }
        
        return count;
    }
}
