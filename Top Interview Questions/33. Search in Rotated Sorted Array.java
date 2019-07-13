class Solution {
    public int search(int[] nums, int target) {
        int rotated = findRotated(nums);
        
        // int rotated = 4;
        /*
        Binary search
        */
        int left = 0, right = rotated - 1;
        while (left <= right) {
            int pivot = (left + right) / 2;
            if (nums[pivot] == target)
                return pivot;
            else {
                if (target < nums[pivot])
                    right = pivot - 1;
                else
                    left = pivot + 1;
            }
        }
        
        left = rotated; right = nums.length - 1;
        while (left <= right) {
            int pivot = (left + right) / 2;
            if (nums[pivot] == target)
                return pivot;
            else {
                if (target < nums[pivot])
                    right = pivot - 1;
                else
                    left = pivot + 1;
            }
        }
        
        return -1;
    }
    
    public static int findRotated(int[] nums) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            //System.out.print(left);
            //System.out.print("\t");
            //System.out.println(right);
            if (nums[left] <= nums[right]) {
                return left;
            } else {
                if (nums[left] <= nums[mid]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
        }
        return left;
    }
    
}