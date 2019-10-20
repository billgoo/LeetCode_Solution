import java.util.Random;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        return quickSelect(nums, 0, nums.length - 1, nums.length - k);
    }
    
    private void swap(int[] nums, int x, int y) {
        int t = nums[x];
        nums[x] = nums[y];
        nums[y] = t;
    }
    
    private int partition(int[] nums, int l, int r) {
        int p_index = (new Random().nextInt(r - l)) + l;
        
        swap(nums, p_index, r);
        int flag = l;
        int p = nums[r];
        for (int i = l; i < r; i++) {
            if (nums[i] < p) swap(nums, flag++, i);
        }
        
        swap(nums, flag, r);
        return flag;
    }
    
    private int quickSelect(int[] nums, int l, int r, int k) {
        if (l == r) return nums[l];
        
        int p = partition(nums, l, r);
        
        if (k == p) return nums[k];
        else if (k < p) 
            return quickSelect(nums, l, p - 1, k);
        
        return quickSelect(nums, p + 1, r, k);
    }
}