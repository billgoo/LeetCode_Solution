class Solution {
    public int singleNumber(int[] nums) {
        int l = nums.length, re = nums[0];
        for (int i = 1; i < l; i++){
            re = re ^ nums[i];
        }
        return re;
    }
}