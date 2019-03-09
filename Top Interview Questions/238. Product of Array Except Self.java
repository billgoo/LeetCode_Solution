class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = 1;
        for (int i = 1; i <= n - 1; i++){
            result[i] = result[i-1] * nums[i-1];
        }
        
        for (int i = n - 2; i >= 0; i--){
            result[i] = result[i] * nums[i+1];
            nums[i] *= nums[i+1];
        }
        
        return result;
    }
}