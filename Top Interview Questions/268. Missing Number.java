class Solution {
    public int missingNumber(int[] nums) {
        int l = nums.length;
        int s = l * (l + 1) / 2;
        for (int n: nums) {
            s -= n;
        }
        return s;
    }
}