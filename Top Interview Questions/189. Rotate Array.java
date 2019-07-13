/**
* two different solutions 
*/

// step jump and swap one by one
class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int count = 0;
        for (int i = 0; count < nums.length; i++) {
            int cur = i;
            int pre = nums[i];
            while (true) {
                int next = (cur + k) % nums.length;
                int temp = nums[next];
                nums[next] = pre;
                pre = temp;
                cur = next;
                count++;
                
                if (i == cur) break;
            }
        }
    }
}

// first inverse the whole array, then seperately inverse the 0 to k and k+1 to the end.
class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int i = 0, j = nums.length - 1;
        while (i <= j) {
            int temp = nums[i];
            nums[i++] = nums[j];
            nums[j--] = temp;
        }
        
        i = 0;
        j = k - 1;
        while (i <= j) {
            int temp = nums[i];
            nums[i++] = nums[j];
            nums[j--] = temp;
        }
        
        i = k;
        j = nums.length - 1;
        while (i <= j) {
            int temp = nums[i];
            nums[i++] = nums[j];
            nums[j--] = temp;
        }
    }
}