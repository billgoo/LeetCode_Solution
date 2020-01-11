import java.util.Arrays;

/**
 * 描述
 * 
 * 给一整数数组, 找到数组中有多少组 不同的元素对 有相同的和, 且和为给出的 target 值, 返回对数.
 * 
 * 样例
 * 
 * 给一数组 nums = [1,1,2,45,46,46], target = 47, 返回 2 1 + 46 = 47 2 + 45 = 47
 */
class Solution {
    /*
     * @param nums: an array of integer
     * @param target: An integer
     * @return: An integer
     */
    public int twoSum6(int[] numbers, int target) {
        if (numbers == null || numbers.length == 0) {
            return 0;
        }
        int left = 0, right = numbers.length - 1;
        int count = 0;
        Arrays.sort(numbers);
        while (left < right) { 
            if (numbers[left] + numbers[right] == target) {
                left++;
                right--;
                count++;
                /* 此处应注意while和if区别:
                 * 只要满足判断条件，while可重复执行多次，而if只执行一次，
                 * 此处if执行一次会导致出现重复解
                 * 下面两个while判断时加left < right是要防止在
                 * left < right且left和right相邻时因为上面的left++和right--
                 * 已经不满足left < right的执行条件依然继续执行下面的语句
                 * 从而导致结果出问题
                 */
                while (left < right && numbers[left - 1] == numbers[left]) {
                    left++;
                }
                while (left < right && numbers[right + 1] == numbers[right]) {
                    right--;
                }
            } else if (numbers[left] + numbers[right] > target) {
                right--;
            } else {
                left++;
            }
        }
        return count;
    }
}
