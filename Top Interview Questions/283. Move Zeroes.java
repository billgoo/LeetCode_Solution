class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0, j = 0, n = nums.length;
        while (i < n && j < n){
            if (nums[i] != 0){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j++] = temp;
            }
            i++;
        }
    }
}